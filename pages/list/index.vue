<template>
	<view class="page">
		<view class="nav_top">
			<scroll-view class="nav_top_list" scroll-x :lower-threshold="300" :scroll-into-view="'nav' + currentIndex"
			 scroll-with-animation="true">
				<view v-for="(item, index) in navList" :key="item.url" class="nav_top_item">
					<view :id="'nav' + index" @click="setIndex(index)" :style="{
							color: currentIndex == index ? '#FF8C00' : '',
							'font-weight': currentIndex == index ? 'bolder' : '',
							'font-size': currentIndex == index ? '30upx' : ''
						}"
					 class="title">
						{{ item.title }}
					</view>
				</view>
			</scroll-view>
			<view class="menu" @click="setEdit">
				<view class="iconfont">&#xe673;</view>
			</view>
		</view>
		<swiper style="height: 100vh;" :current="currentIndex" @change="tabChange">
			<swiper-item v-for="(i, index) in navList" :key="index">
				<scroll-view style="height: 100vh;" scroll-y @scrolltolower="getData()">
					<view class="book_list">
						<view v-for="(i, index) in bookList" :key="i.pk" class="book_item">
							<view @click="goToChapter(i.pk, index)">
								<view class="cover">
									<image style="width: 240rpx;height: 270rpx;" :src="i.fields.cover_url"></image>
								</view>
								<view class="book_name">{{ i.fields.book_name | ellipsis }}</view>
								<view class="last_chapter">{{ i.fields.last_chapter | ellipsis }}</view>
							</view>
						</view>
					</view>
				</scroll-view>
			</swiper-item>
		</swiper>
		<view v-if="isEdit" class="edit-menu">
			<view class="edit-menu-top">
				<view @click="setEdit" style="font-size: 70rpx;">×</view>
				<view @click="setEdit">完成</view>
			</view>
			<view class="edit-menu-title">
				<view>我的频道</view>
				<view style="color: #707070;font-size: 30rpx;margin-left: 10rpx;font-weight: normal;">点击删除频道</view>
			</view>
			<view class="edit-menu-list">
				<view class="edit-menu-item" v-for="(i,index) in navList" :key="i.url" @click="deleteMenu(index)">{{ i.title }}</view>
			</view>
			<view class="edit-menu-title">
				<view>全部频道</view>
				<view style="color: #707070;font-size: 30rpx;margin-left: 10rpx;font-weight: normal;">点击添加频道</view>
			</view>
			<view class="edit-menu-all-list">
				<view class="edit-menu-all-item" v-for="(i,index) in allnavlist" :key="i.url" @click="addMenu(index)">{{ i.title }}</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				loadMore: {
					iconSize: 24,
					status: 'more',
					showIcon: true,
					iconType: 'snow',
					color: 'red',
					contentText: {
						contentdown: '上拉显示更多',
						contentrefresh: '正在加载...',
						contentnomore: '没有更多数据了'
					}
				},
				bookList: [{
					"model": "app.bookmodel",
					"pk": 65,
					"fields": {
						"book_name": "\u6697\u591c\u534f\u594f\u66f2",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20181206/5c0888b707906-600x800.jpg!cover-400",
						"description": "\n\u3000\u3000\u6c38\u6052\u7684\u5bfb\u627e\uff0c\u5bf9\u6297\u751f\u547d\u7684\u77ed\u6682\u8f6e\u56de\uff0c\u4e3a\u7684\u662f\u4e94\u767e\u5e74\u524d\u4e0d\u80af\u9057\u5fd8\u7684\u627f\u8bfa\u3002\u5e73\u51e1\u5973\u5b69\u4e0e\u5438\u8840\u738b\u5b50\u7684\u5947\u5f02\u9082\u9005\uff0c\u8ff7\u7cca\u5973\u5b69\u7684\u5e73\u9759\u751f\u6d3b\u5c06\u4f1a\u53d1\u751f\u600e\u6837\u7684\u6539\u53d8\uff1f\u8fd9\u5f98\u5f8a\u5728\u9752\u6885\u7af9\u9a6c\u7684\u90bb\u5bb6\u7537\u5b69\u548c\u5438\u8840\u738b\u5b50\u4e4b\u95f4\u7684\u5e73\u51e1\u5973\u5b69\uff0c\u53c8\u5c06\u4f55\u53bb\u4f55\u4ece\uff1f\u3000\u3000\n500\u5e74\u524d\uff0c\u5438\u8840\u9b3c\u7231\u4e0a\u4e86\u4e00\u4e2a\u4eba\u7c7b\u7684\u5973\u5b69\uff0c\u4f46\u662f\u56e0\u4e3a\u751f\u547d\u5468\u671f\u4e0d\u540c\uff0c\u4eba\u7c7b\u7684\u5973\u5b69\u6700\u540e\u6b7b\u4e86\u3002\u60b2\u4f24\u7684\u5438\u8840\u9b3c\u4e0d\u60f3\u518d\u53d7\u6b64\u4f24\u75db\uff0c\u60f3\u8981\u56de\u590d\u4eba\u7c7b\u7684\u8eab\u4efd\u3002\u7ec8\u4e8e\u627e\u5230\u53d8\u56de\u4eba\u7684\u65b9\u6cd5\u2026\u2026\n\u6211\u4eec\u7684\u6545\u4e8b\u5219\u53d1\u751f\u5728500\u5e74\u540e\u7684\u73b0\u4ee3\u3002\u4e00\u4e2a\u666e\u901a\u7684\u5973\u5b69\u539f\u672c\u8fc7\u7740\u5e73\u6de1\u7684\u6bcf\u4e00\u5929\uff0c\u5374\u88ab\u4e00\u53ea\u5438\u8840\u9b3c\u6270\u4e71\u4e86\u5979\u539f\u672c\u5e73\u9759\u7684\u751f\u6d3b\u3002\u7c89\u7ea2\u7684\u6d6a\u6f2b\u7231\u60c5\u534f\u594f\u66f2\u5373\u5c06\u54cd\u8d77\uff01",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 70,
					"fields": {
						"book_name": "\u963fSA\u4e13\u7528",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20181206/5c0888b7348bf-600x800.jpg!cover-400",
						"description": "\n\u521d\u4e00\u7537\u751f\u201c\u72d0\u201d\u548c\u5fc3\u4eea\u5973\u5b69\u201c\u963fsa\u201d\u7684\u7b2c\u4e00\u6b21\u7ea6\u4f1a\uff0c\u5374\u88ab\u53f2\u4e0a\u6700\u8131\u7ebf\u6700\u5e05\u6c14\u7684\u9ed1\u767d\u65e0\u5e38\u544a\u77e5\uff0c\u4ed6\u5df2\u7ecf\u6b7b\u4e86\uff01\uff01\uff01\u88ab\u6293\u5230\u9634\u68ee\u6050\u6016\u7684\u960e\u738b\u6bbf\uff0c\u4ed6\u8981\u600e\u4e48\u5151\u73b0\u81ea\u5df1\u7684\u8bfa\u8a00\u2026\u2026\u3000\u3000\u6d6a\u6f2b\u7231\u60c5\u5267\uff0c\u4e3a\u5b88\u62a4\u7231\u7684\u4eba\u800c\u590d\u6d3b\u7684\u7537\u4e3b\u89d2\u3002\u6700\u73cd\u60dc\u7684\u4eba\uff0c\u6700\u73cd\u8d35\u7684\u7231\u60c5\uff0c\u674e\u96f7\u96f7\u9996\u6b21\u5728MK\u53d1\u8868\u7684\u8fde\u8f7d\u4f5c\u54c1\uff0c\u6f14\u7ece\u771f\u6b63\u7684\uff1a\u6b7b\u4e86\u90fd\u8981\u7231\uff01",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 96,
					"fields": {
						"book_name": "\u6781\u54c1\u7f8e\u5c11\u5973",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20180718/5b4eafeeedeb2-599x798.jpg!cover-400",
						"description": "\n\u7537\u4e3b\u89d2\u738b\u5f3a\u662f\u5b66\u6821\u6253\u67b6\u80fd\u624b\uff0c\u6df7\u4e16\u9b54\u738b\uff0c\u4f46\u4ed6\u8fd8\u6709\u4e00\u4e2a\u5f31\u70b9\uff0c\u6015\u8eab\u4e3a\u73ed\u957f\u7684\u70b9\u84dd\u3002\u4e00\u6b21\u5728\u5de5\u5730\u4e0e\u70b9\u84dd\u7684\u51b2\u7a81\u4e2d\uff0c\u738b\u5f3a\u56e0\u4e3a\u81ea\u5df1\u6316\u9f3b\u5c4e\u800c\u610f\u5916\u7838\u6b7b\uff08=V=\uff09\u2022\u2022\u2022\u4f46\u662f\u56e0\u4e3a\u4ed6\u5f39\u9f3b\u5c4e\u81ea\u6740\u7684\u5671\u5934\u6cbb\u597d\u4e86\u5927\u5929\u4f7f\u957f\u7684\u5fe7\u90c1\u75c7\u2022\u2022\u2022\u4e8e\u662f\u5927\u5929\u4f7f\u957f\u7ed9\u4ed6\u4e00\u6b21\u590d\u6d3b\u7684\u673a\u4f1a\u2022\u2022\u2022\uff0c\u56e0\u4e3a\u5929\u4f7f\u6ca1\u6234\u773c\u955c\u770b\u4e0d\u6e05\u695a\uff0c\u738b\u5f3a\u7684\u7075\u9b42\u610f\u5916\u8dd1\u8fdb\u4e86\u5973\u4e3b\u89d2\u70b9\u84dd\u7684\u8eab\u4f53\u91cc\u2022\u53ef\u601c\u7684\u70b9\u84dd\u4fbf\u9644\u8eab\u5728\u4e00\u4e2a\u80cc\u5305\u4e0a\u9762\u2022\u2022\u738b\u5f3a\u88ab\u544a\u77e5\u5fc5\u987b\u7528\u70b9\u84dd\u7684\u8eab\u4f53\u5bfb\u627e\u5230\u4e00\u4efd\u771f\u7231\u624d\u53ef\u4ee5\u6062\u590d\u7537\u513f\u8eab\u3002\u4e3a\u4e86\u6062\u590d\u7537\u513f\u8eab\u2022\u2022\u2022\u4ed6\u5f00\u59cb\u4e86\u5168\u65b0\u7684\u751f\u6d3b",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 1782,
					"fields": {
						"book_name": "\u591c\u5e55\u897f\u997c\u5c4b",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20190528/5cecdb98a6403-600x800.png!cover-400",
						"description": "\n\u6545\u4e8b\u8bb2\u8ff0\u7684\u662f\u4e00\u95f4\u795e\u79d8\u800c\u8be1\u5f02\u7684\u591c\u5e55\u897f\u997c\u5c4b\u4e3a\u884c\u884c\u8272\u8272\u7684\u987e\u5ba2\u63d0\u4f9b\u5177\u6709\u9b54\u6cd5\u7684\u9ed1\u6697\u897f\u70b9\uff0c\u4e8e\u662f\u4e0d\u540c\u7684\u4eba\u5229\u7528\u4e0d\u540c\u7684\u9ed1\u6697\u897f\u70b9\u9009\u62e9\u4e86\u4e0d\u540c\u7684\u4eba\u751f\u60b2\u559c\u5267\uff0c\u800c\u591c\u5e55\u897f\u997c\u5c4b\u4e5f\u88ab\u5927\u5bb6\u79f0\u4e3a\u5929\u5802\u4e0e\u5730\u72f1\u7684\u5206\u5c94\u53e3\uff01",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 2535,
					"fields": {
						"book_name": "\u841d\u8389\u6740\u624b",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20181206/5c0889e49022e-210x277.jpg!cover-400",
						"description": "\n\u5728\u4e3b\u4eba\u548c\u5973\u4ec6\u7684\u8fd9\u6837\u7684\u5173\u7cfb\u4e0b\uff0c\u6211\u4eec\u662f\u4e0d\u662f\u4ece\u6765\u5c31\u4e0d\u8bb0\u5f97\u81ea\u5df1\u60f3\u8981\u7684\u4e1c\u897f\uff1f\n\u5951\u7ea6\uff0c\u4eba\u5076\uff0c\u8ffd\u6740\uff0c\u5230\u5e95\u6c90\u5bb6\u7684\u79d8\u5bc6\u662f\u4ec0\u4e48\uff1f\n\u5c0f\u767d\u548c\u6d1b\u4e3d\u5854-\u6b63\u592a\u4e0e\u4eba\u5f62\u7684\u68a6\u5e7b\u6545\u4e8b\u6b63\u5728\u4e0a\u6f14\uff01\n\u841d\u8389\u6740\u624b\u5b98\u65b9\u8ba8\u8bba\u7fa4\n\u841d\u8389\u7684\u8fdc\u5f811\u53f7\u7fa4\uff08\u590f\u96ea\uff0911814767\n\u841d\u8389\u7684\u8fdc\u5f812\u53f7\u7fa4\uff08\u771f\u840c\uff0966755902\n\u841d\u8389\u7684\u8fdc\u5f813\u53f7\u7fa4\uff08\u8212\u9038\uff0918433787\n\u841d\u8389\u7684\u8fdc\u5f814\u53f7\u7fa4\uff08\u6c99\u7f57\uff0956519860\n\u841d\u8389\u7684\u8fdc\u5f815\u53f7\u7fa4\uff08\u534e\u97f3\uff0960886413\n\u841d\u8389\u7684\u8fdc\u5f815\u53f7\u7fa4\uff08\u841d\u8389\u6740\u624b\uff0935967997\uff08\u65b0\uff09\n\u8212\u9038\u540e\u63f4\u56e2\uff08\u8bfb\u8005\u7fa4\uff0985749213\uff08\u65b0\uff09\n\u300a\u841d\u8389\u6740\u624b\u300b\u7cfb\u5217\u6e38\u620f\u6f2b\u753b\u4ea4\u6d41\u8bba\u575b\nhttp://girlsoul.5d6d.com",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 8613,
					"fields": {
						"book_name": "\u9519\u9b42",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20181206/5c088a237180f-210x277.jpg!cover-400",
						"description": "\n\u5176\u5b9e\u662f\u4e00\u4e2a\u5f88\u65e0\u804a\u7684\u6545\u4e8b\uff0c\u5f88\u65e0\u804a\u5f88\u65e0\u804a\u3002\u3002\u3002\u3002\u3002\u3002",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 8830,
					"fields": {
						"book_name": "\u6c38\u6052\u4e4b\u8f6e",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20181206/5c088a2fae568-210x277.jpg!cover-400",
						"description": "\n\u65f6\u7a7a\u4e4b\u5916\uff0c\u4ecd\u7136\u662f\u6570\u4e0d\u6e05\u7684\u65f6\u7a7a\u3002\u65e0\u9650\u795e\u79d8\u7684\u6c38\u6052\u4e4b\u8f6e\uff0c\u63a7\u5236\u7740\u6240\u6709\u65f6\u7a7a\u4e2d\u4e07\u7269\u7684\u547d\u8fd0\u2026\u2026\u6545\u4e8b\u60a0\u957f\u3002\u800c\u6211\u4eec\uff0c\u53ea\u662f\u60f3\u63a2\u8ba8\u4e00\u4e2a\u4e3b\u9898\uff1a\u638c\u63e1\u81ea\u5df1\u7684\u547d\u8fd0\uff01\uff08\u6bcf\u5468\u4e94\u66f4\u65b0\uff0c\u5468\u4e2d\u4e0d\u5b9a\u671f\u66f4\u65b0\u8bbe\u5b9a\u53ca\u63d2\u753b\uff09\
							n\ u300a\ u6c38\ u6052\ u4e4b\ u8f6e\ u300b\ u7535\ u5b50\ u5355\ u884c\ u672c\ u5df2\ u7ecf\ u767b\ u5f55~~\n\ uff1ahttp: //ebook.zymk.cn/ebook/elist/24-0-1.html",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 9666,
					"fields": {
						"book_name": "\u4e91\u6d77\u4e4b\u4e0a",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20181206/5c088a3faeb17-210x277.jpg!cover-400",
						"description": "\n\u50cf\u68c9\u82b1\u7cd6\u4e00\u6837\u8f6f\u8f6f\u767d\u767d\u7684\u4e91\u6735\u5728\u84dd\u5929\u4e0a\u821e\u8e48\uff0c\u5f3a\u5927\u706f\u5149\u5e08\u592a\u9633\u541b\u7528\u91d1\u8272\u9633\u5149\u95ea\u70c1\u5176\u95f4\u2026\u2026\u53ef\u662f\u4e0d\u77e5\u4ece\u4ec0\u4e48\u65f6\u5019\u5f00\u59cb\uff0c\u5929\u7a7a\u6e10\u6e10\u88ab\u539a\u91cd\u7684\u4e91\u5c42\u7b3c\u7f69\uff0c\u4eba\u4eec\u79f0\u4e4b\u4e3a\u4e91\u6d77\u3002\u968f\u7740\u65f6\u95f4\u7684\u6d41\u901d\uff0c\u4eba\u4eec\u9010\u6e10\u6de1\u5fd8\u4e86\u84dd\u5929\u767d\u4e91\uff0c\u4e0d\u518d\u6709\u4eba\u77e5\u9053\u4e91\u6d77\u4e0a\u9762\u5230\u5e95\u6709\u4ec0\u4e48\uff0c\u4e5f\u6ca1\u6709\u4eba\u77e5\u9053\u4e91\u6d77\u4ece\u4f55\u800c\u6765\u2026\u2026\n\u4e3b\u4eba\u516c\u5c3c\u5965\u6bcf\u5929\u6700\u559c\u6b22\u505a\u7684\u4e8b\uff0c\u5c31\u662f\u5927\u58f0\u5ba3\u8bb2\u7236\u4eb2\u5728\u4e91\u6d77\u4e0a\u9762\u7684\u6240\u89c1\u6240\u95fb\uff0c\u5927\u5bb6\u90fd\u4e0d\u4ee5\u4e3a\u7136\uff0c\u5e76\u4e92\u76f8\u8bae\u8bba\u4ed6\u7684\u7236\u4eb2\u662f\u4e2a\u6b3a\u4e16\u76d7\u540d\u7684\u5927\u9a97\u5b50\u3002\u5c3c\u5965\u4e3a\u4e86\u8bc1\u660e\u81ea\u5df1\u7684\u7236\u4eb2\u6ca1\u6709\u8bf4\u8c0e\uff0c\u4e0b\u5b9a\u51b3\u5fc3\u4e00\u5b9a\u8981\u51b2\u7834\u4e91\u6d77\u7684\u963b\u6321\uff0c\u627e\u5230\u771f\u76f8\uff01\u4e00\u8def\u4e0a\u4ed6\u53d1\u73b0\u4e91\u6d77\u7684\u5b58\u5728\uff0c\u5176\u5b9e\u662f\u5409\u5c3c\u4e9a\u4eba\u7684\u5de8\u5927\u9634\u8c0b\uff0c\u800c\u4ed6\u7684\u4f19\u4f34\u770b\u4f3c\u670b\u53cb\u53c8\u50cf\u654c\u4eba\u2026\u2026\n\u4e0d\u8981\u89c9\u5f97\u8fd9\u53ea\u662f\u4e2a\u73af\u4fdd\u8bdd\u9898\u7684\u5192\u9669\u6545\u4e8b\u3002\u5982\u679c\u6211\u4eec\u4e0d\u597d\u597d\u73cd\u60dc\u73b0\u5728\u62e5\u6709\u7684\u4e00\u5207\u7684\u8bdd\uff0c\u6216\u8bb8\u6211\u4eec\u771f\u7684\u65e0\u6cd5\u907f\u514d\u8d44\u6e90\u532e\u4e4f\uff0c\u79d1\u6280\u5012\u9000\uff0c\u88ab\u6c38\u8fdc\u7981\u9522\u5728\u539a\u91cd\u4e91\u6d77\u7684\u60b2\u60e8\u547d\u8fd0\u2026\u2026",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 26515,
					"fields": {
						"book_name": "\u9ea6\u62c9\u98ce\u5a5a\u540e80",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20181218/5c18d6c2a6987-207x277.jpg!cover-400",
						"description": "\n\u300a\u9ea6\u62c9\u98ce\u300b\u7cfb\u5217\u4e4b\u300a\u5a5a\u540e80\u300b",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 27578,
					"fields": {
						"book_name": "\u7231\u6597\u7f57\u4e0d\u53d8",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20181206/5c088d7511088-210x277.jpg!cover-400",
						"description": "\n\u8fd9\u4e9b\u90fd\u662f\u5728A4\u7eb8\u4e0a\u753b\u7684\uff0c\u6ca1\u6709\u4e0a\u8272\u5e0c\u671b\u5927\u5bb6\u559c\u6b22",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 69385,
					"fields": {
						"book_name": "\u8150\u5973\u7b14\u8bb0",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20181206/5c08c43525805-210x277.jpg!cover-400",
						"description": "\n\u8fd9\u662f\u4e00\u79cd\u795e\u5947\u7684\u751f\u7269\uff01\uff01\uff1f\uff1f\u76f4\u7537\u76f4\u5973\u8bf7\u70b9\u51fb\u5c4f\u5e55\u53f3\u4e0a\u89d2\u6027\u611f\u5c0f\u7ea2\u53c9\u7ed5\u884c\uff01\uff01\uff01",
						"last_chapter": null
					}
				}, {
					"model": "app.bookmodel",
					"pk": 99143,
					"fields": {
						"book_name": "\u6781\u5ea6\u5206\u88c2",
						"cover_url": "https://oss.mkzcdn.com/comic/cover/20180723/5b559af9eedb1-600x800.jpg!cover-400",
						"description": "\n\u672b\u4e16\u754c\uff0c\u6709\u7740\u7e41\u534e\uff0c\u8150\u673d\uff0c\u7eb8\u9189\u91d1\u8ff7\u7684\u5927\u57ce\u5e02\uff1b\u6709\u7740\u9893\u8d25\uff0c\u80ae\u810f\uff0c\u4e4c\u70df\u7634\u6c14\u7684\u4e5d\u53cd\u4e4b\u5730\uff1b\u6709\u7740\u7578\u5f62\uff0c\u5815\u843d\uff0c\u5149\u602a\u9646\u79bb\u7684\u5e7b\u60f3\u754c\u3002\n\u4eba\u7c7b\u53d7\u5230\u4e00\u79cd\u672a\u77e5\u7684\u7279\u6b8a\u75c5\u6bd2\u611f\u67d3\uff08\u611f\u67d3\u6e90\u672a\u786e\u5b9a\uff0c\u6545\u4e8b\u540e\u9762\u624d\u5f00\u59cb\u5256\u6790\uff09\uff0c\u8fd9\u79cd\u75c5\u6bd2\u4f7f\u4eba\u7c7b\u751f\u75c5\uff08\u4e0d\u6b62\u662f\u8089\u4f53\u4e0a\u7684\uff09\uff0c\u53d1\u751f\u7279\u6b8a\u53d8\u5f02\uff0c\u5e76\u5c06\u75be\u75c5\u5371\u5bb3\u65e0\u9650\u653e\u5927\uff0c\u6700\u540e\u4f7f\u5f97\u4efb\u4f55\u5fae\u5c0f\u7684\u75be\u75c5\u6b7b\u4ea1\u7387\u90fd\u8fbe\u5230\u4e86100%\uff0c\u53d7\u5230\u8fd9\u79cd\u53d8\u5f02\u73b0\u8c61\u7684\u4eba\u7c7b\u7edf\u79f0\u4e3a\u3010\u6781\u9650\u60a3\u8005\u3011\u3002\n\u5f53\u8840\u8272\u5165\u4fb5\uff0c\u6781\u9650\u75c5\u4eba\u8fdb\u884c\u6740\u622e\uff0c\u533b\u751f\u708e\u65e0\u60d1\u5f00\u59cb\u89e3\u5256\u5f62\u5f62\u8272\u8272\u7684\u201c\u75c5\u4eba\u201d\uff0c\u662f\u6551\u8d4e\u6291\u6216\u60e9\u7f5a?!\u60ac\u7591\u4e0e\u63a8\u7406\u63ed\u5f00\u60ca\u609a\u5e55\u5e03\u4e0b\u7684\u771f\u76f8\u2026\u2026",
						"last_chapter": null
					}
				}],
				currentIndex: 0,
				navList: [],
				page: 6,
				id: 12,
				swiperheight: 500,
				isEdit: false,
				allnavlist: [],
			};
		},
		computed: {},
		methods: {
			// isLoading(e) {
			// 	this.isLoad = e.detail.value;
			// },
			getData() {
				uni.request({
					url: this.$weburl + 'showBooklist/' + this.id + '/' + (this.id + this.page),
					success: res => {
						this.bookList = this.bookList.concat(res.data);
						this.id += this.page;

					}
				});
			},
			setIndex(i) {
				this.currentIndex = i;
				uni.setStorage({
					key: 'current',
					data: this.currentIndex
				})
			},
			tabChange(e) {
				this.currentIndex = e.detail.current;
				uni.setStorage({
					key: 'current',
					data: this.currentIndex
				})
			},
			goToChapter(i, index) {
				uni.navigateTo({
					url: '../chapter/index?id=' + i
				});
				uni.setStorage({
					key: 'cover' + i,
					data: this.bookList[index].fields.cover_url
				});
				uni.setStorage({
					key: 'book_name' + i,
					data: this.bookList[index].fields.book_name
				});
			},
			setEdit() {
				this.isEdit = this.isEdit ? false : true
			},
			deleteMenu(i) {
				if (this.navList.length <= 4) {
					uni.showToast({
						icon: 'none',
						title: '至少保留4个标签',
					})
				} else {
					this.navList.splice(i, 1)
					this.allnavlist.push(this.navList[i])
				}

			},
			addMenu(i) {
				this.navList.push(this.allnavlist[i])
				this.allnavlist.splice(i, 1)
			}
		},

		beforeCreate() {
			uni.request({
				url: this.$weburl + 'showBooklist/0/12',
				success: res => {
					this.bookList = res.data;
				}
			});
		},
		onPageScroll(e) {
			this.pageScrollTop = Math.floor(e.scrollTop);
		},
		filters: {
			ellipsis(str) {
				if (!str) return '';
				if (str.length > 7) {
					return str.slice(0, 7) + '...';
				}
				return str;
			}
		},
		onReachBottom() {
			this.loadMore.status = 'loading';
		},
		onLoad() {
			
			uni.getStorage({
				key: 'current',
				success: (res) => {
					this.currentIndex = res.data
				}
			})
			uni.getStorage({
				key: 'navList',
				success: () => {
					this.navList = res.data;
				},
				fail: res => {
					this.navList = [{
							title: '全部',
							url: '全部'
						},
						{
							title: '霸总',
							url: '霸总'
						},
						{
							title: '修真',
							url: '修真'
						},
						{
							title: '恋爱',
							url: '恋爱'
						},
						{
							title: 'VIP',
							url: 'VIP'
						},
						{
							title: '付费',
							url: '付费'
						},
						{
							title: '连载',
							url: '连载'
						},
						{
							title: '完结',
							url: '完结'
						},
						{
							title: '校园',
							url: '校园'
						},
						{
							title: '冒险',
							url: '冒险'
						},
						{
							title: '搞笑',
							url: '搞笑'
						}
					];
				}
			});

			uni.getStorage({
				key: 'allnavlist',
				success: () => {

				},
				fail: () => {
					this.allnavlist = [{
							title: '生活',
							url: '生活'
						},
						{
							title: '热血',
							url: '热血'
						},
						{
							title: '架空',
							url: '架空'
						},
						{
							title: '后宫',
							url: '后宫'
						},
						{
							title: '耽美',
							url: '耽美'
						},
						{
							title: '恐怖',
							url: '恐怖'
						},
						{
							title: '动作',
							url: '动作'
						},
						{
							title: '穿越',
							url: '穿越'
						},
						{
							title: '励志',
							url: '励志'
						},
						{
							title: '同人',
							url: '同人'
						},
						{
							title: '真人',
							url: '真人'
						},
						{
							title: '免费',
							url: '免费'
						},
						{
							title: '灵异',
							url: '灵异'
						},
						{
							title: '古风',
							url: '古风'
						},
						{
							title: '战争',
							url: '战争'
						},
						{
							title: '科幻',
							url: '科幻'
						},
						{
							title: '悬疑',
							url: '悬疑'
						},
						{
							title: '玄幻',
							url: '玄幻'
						},
						{
							title: '竞技',
							url: '竞技'
						},
						{
							title: '百合',
							url: '百合'
						},
						{
							title: '连载',
							url: '连载'
						},
					];
				}
			})
		},
		onShow() {
			uni.getStorage({
				key: 'type',
				success: (res) => {
					this.currentIndex = res.data
					uni.removeStorage({
						key: 'type',
					})
				},
				fail: () => {
					this.currentIndex = 0
				}
			})
		}
	};
</script>

<style scoped lang="scss">
	.nav_top {
		.nav_top_list {
			position: fixed;
			top: 0;
			left: 0;
			z-index: 100;
			width: 85%;
			height: 90upx;
			box-shadow: 0 0 8upx rgba(0, 0, 0, 0.06);
			background-color: #fff;
			white-space: nowrap;
			padding-left: 20rpx;

			.nav_top_item {
				height: 90upx;
				text-align: center;
				padding: 0upx 20upx;
				color: #303133;
				display: inline-block;
				position: relative;
				font-size: 28upx;
				transform: scale(1);
				transition: 0.3s;

				.title {
					line-height: 90upx;
				}
			}

			.current {
				color: $uni-theme-color;
				transform: scale(1.1);
			}
		}

		.menu {
			position: fixed;
			z-index: 100;
			right: 0;
			top: 0;
			width: 100rpx;
			height: 90rpx;
			display: flex;
			justify-content: center;
			align-items: center;
			background: #ffffff;

			box-shadow: 0 2rpx 1rpx rgba(0, 0, 0, 0.06);
			box-shadow: 2 0rpx rgba(255, 255, 255, 0.06);

			.iconfont {
				color: #FF8C00;
			}
		}
	}

	.book_list {
		padding-top: 100rpx;
		display: flex;
		
		flex-flow: wrap;
		padding-bottom: 150rpx;
		justify-content: space-between;
	}

	.book_item {
		padding-top: 20rpx;

	}

	.book_name {
		display: flex;
		font-size: 30rpx;
		justify-content: center;
		align-items: center;
		width: 240rpx;
	}

	.last_chapter {
		padding: 5rpx;
		display: flex;
		font-size: 25rpx;
		justify-content: center;
		align-items: center;
		color: #2c405a;
	}

	.loadmore {
		padding-top: 50rpx;
		display: flex;
		width: 750rpx;
		justify-content: center;
	}

	.edit-menu {
		z-index: 102;
		display: flex;
		flex-direction: column;
		width: 750rpx;
		align-items: center;
		background: #FFFFFF;
		height: 100vh;
		position: fixed;
		top: 0;
		left: 0;

		.edit-menu-top {
			display: flex;
			justify-content: space-between;
			align-items: center;
			width: 700rpx;
			color: #FF8C00;
			height: 70rpx;

		}

		.edit-menu-title {
			display: flex;
			align-items: center;
			width: 700rpx;
			height: 80rpx;
			font-size: 35rpx;
			font-weight: bolder;
		}

		.edit-menu-list {
			display: flex;
			flex-wrap: wrap;
			width: 700rpx;
			justify-content: space-between;

			.edit-menu-item {
				width: 140rpx;
				margin: 10rpx;
				background: #eeeeee;
				text-align: center;
				padding: 20rpx 10rpx;
				font-size: 30rpx;
			}
		}

		.edit-menu-list:after {
			padding: 20rpx 10rpx;
			content: '';
			width: 140rpx;
			margin: 10rpx;
		}

		.edit-menu-all-list {
			display: flex;
			flex-wrap: wrap;
			width: 700rpx;
			justify-content: space-between;

			.edit-menu-all-item {
				width: 138rpx;
				margin: 10rpx;
				background: #eeeeee;
				text-align: center;
				padding: 20rpx 10rpx;
				font-size: 30rpx;
				box-shadow: 1rpx 1rpx 1rpx 1rpx #000000;
				background: #FFFFFF;
			}

		}

		.edit-menu-all-list:after {
			padding: 20rpx 10rpx;
			content: '';
			width: 138rpx;
			margin: 10rpx;
		}
	}

	page {
		background-color: #fff;
	}
</style>
