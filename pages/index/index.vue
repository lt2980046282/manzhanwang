<template>
	<view>
		<view :class="this.scrollTop > 150 ? 'fixd_top_nav' : 'index_top_nav'" style="display: flex;align-items: center;height: 100rpx;">
			<view v-if="sex == 0" @click="sex = 1" class="index_top_nav_item1 iconfont" style="z-index:100; padding-left: 30upx;font-size: 67upx;color: pink;">
				{{ sex == 0 ? '&#xe618;' : '&#xe609;' }}
			</view>
			<view v-if="sex == 0" @click="sex = 1" class="index_top_nav_item1 iconfont" style="margin-left: -185upx;  padding-left: 30upx;font-size: 74upx;color: #007AFF;">
				{{ !sex == 0 ? '&#xe618;' : '&#xe609;' }}
			</view>

			<view v-if="sex == 1" @click="sex = 0" class="index_top_nav_item1 iconfont" style="z-index:100; padding-left: 30upx;font-size: 75upx;color: #007AFF;">
				{{ sex == 0 ? '&#xe618;' : '&#xe609;' }}
			</view>
			<view v-if="sex == 1" @click="sex = 0" class="index_top_nav_item1 iconfont" style=" padding-left: 30upx;font-size: 67upx;color: pink;margin-left: -185upx;">
				{{ !sex == 0 ? '&#xe618;' : '&#xe609;' }}
			</view>

			<view
				style="display: flex;align-items: center;height: 30rpx;"
				class="index_top_nav_item"
				v-for="(i, index) in navList"
				:key="index"
				@click="navIndex = index"
				:style="{ color: index == navIndex ? '#FF0000' : '' }"
			>
				<view class="control">
					<view style="font-size: 36upx;">{{ i.name }}</view>
					<!-- <view style="" class="iconfont">&#xe675;</view> -->
				</view>
			</view>
			<view @click="setShowsearch()" class="index_top_nav_item1 iconfont" style="color: #FF0000;margin-right: 20rpx;display: flex;align-items: center;font-size: 35rpx;">
				&#xe60a;
			</view>
		</view>
		<swiper style="height: 100vh;" :current="navIndex" @change="tabChange">
			<swiper-item v-for="i in 2" :key="i">
				<scroll-view style="height: 100vh;border-radius:0rpx 0rpx 10% 10%;" scroll-y="" :lower-threshold="1000" @scrolltolower="getData">
					<swiper
						style="height: 500upx;padding-top: 100rpx;border-radius:0rpx 0rpx 10% 10%;"
						indicator-dots=""
						indicator-color="pink"
						autoplay=""
						indicator-active-color="white"
					>
						<swiper-item v-for="(i, index) in coverList" :key="i.pk" @click="goToChapter(i.pk, index)">
							<image lazy-load="" style="width: 750upx;border-radius:0rpx 0rpx 10% 10%;" :src="i.fields.cover_url"></image>
						</swiper-item>
					</swiper>
					<view class="menu_list">
						<view v-for="(i, index) in nav" :key="index" style="" class="menu_item">
							<navigator :url="i.url">
								<button class="control" :style="{ color: i.color }">
									<view class="iconfont" style="font-size: 45rpx;">{{ i.icon }}</view>
									<view style="font-size: 20rpx;color: black;">{{ i.name }}</view>
								</button>
							</navigator>
						</view>
					</view>
					<view class="common">
						<view class="book_list">
							<block v-for="(i, index) in bookList" :key="index">
								<view v-if="0 == index" class="book_menu">
									<view class="title">
										<view class="iconfont">&#xe629;</view>
										客栈精品
									</view>
									<navigator url="../list/index" open-type="switchTab"><view class="more">更多</view></navigator>
								</view>
								<view class="book_item" @click="goToChapter(i.pk, index)" v-if="index <= 3">
									<view><image mode="aspectFill" lazy-load="" :src="i.fields.cover_url"></image></view>
									<view class="book_name">{{ i.fields.book_name | ellipsis }}</view>
									<view class="book-description">{{ '作者很懒不想写任何书籍描述' | ellipsis }}</view>
								</view>
								<view v-if="4 == index" class="book_menu">
									<view class="title ">
										<view class="iconfont">&#xe629;</view>
										独家作品
									</view>
									<navigator url="../list/index" open-type="switchTab"><view class="more">更多</view></navigator>
								</view>
								<view class="unique-book-item1" @click="goToChapter(i.pk, index)" v-if="index == 4">
									<view><image lazy-load="" :src="i.fields.cover_url"></image></view>
									<view class="unique-book-name">{{ i.fields.book_name | ellipsis }}</view>
									<view class="unique-book-description">{{ '作者很懒不想写任何书籍描述' | ellipsis }}</view>
								</view>
								<view class="unique-book-item" @click="goToChapter(i.pk, index)" v-if="(index <= 10) & (index > 4)">
									<view><image lazy-load="" :src="i.fields.cover_url"></image></view>
									<view class="unique-book-name">{{ i.fields.book_name | ellipsis }}</view>
									<view class="unique-book-description">{{ '作者很懒不想写任何书籍描述' | ellipsis }}</view>
								</view>
								<view class="unique-book-item-last" @click="goToChapter(i.pk, index)" v-if="index === 11">
									<view><image mode="aspectFill" lazy-load="" :src="i.fields.cover_url"></image></view>
								</view>
								<view v-if="12 == index" class="book_menu">
									<view class="title ">
										<view class="iconfont">&#xe629;</view>
										新作尝鲜
									</view>
									<navigator url="../list/index" open-type="switchTab"><view class="more">更多</view></navigator>
								</view>
								<view class="unique-book-item1" @click="goToChapter(i.pk, index)" v-if="index == 12">
									<view><image mode="" lazy-load="" :src="i.fields.cover_url"></image></view>
									<view class="unique-book-name">{{ i.fields.book_name | ellipsis }}</view>
									<view class="unique-book-description">{{ '作者很懒不想写任何书籍描述' | ellipsis }}</view>
								</view>
								<view class="unique-book-item" @click="goToChapter(i.pk, index)" v-if="(index <= 15) & (index > 12)">
									<view><image lazy-load="" :src="i.fields.cover_url"></image></view>
									<view class="unique-book-name">{{ i.fields.book_name | ellipsis }}</view>
									<view class="unique-book-description">{{ '作者很懒不想写任何书籍描述' | ellipsis }}</view>
								</view>
								<view v-if="16 == index" class="book_menu">
									<view class="title ">
										<view class="iconfont">&#xe629;</view>
										VIP作品
									</view>
									<navigator url="../list/index" open-type="switchTab"><view class="more">更多</view></navigator>
								</view>
								<view class="unique-book-item1" @click="goToChapter(i.pk, index)" v-if="index == 16">
									<view><image mode="" lazy-load="" :src="i.fields.cover_url"></image></view>
									<view class="unique-book-name">{{ i.fields.book_name | ellipsis }}</view>
									<view class="unique-book-description">{{ '作者很懒不想写任何书籍描述' | ellipsis }}</view>
								</view>
								<view class="unique-book-item" @click="goToChapter(i.pk, index)" v-if="(index <= 19) & (index > 16)">
									<view><image lazy-load="" :src="i.fields.cover_url"></image></view>
									<view class="unique-book-name">{{ i.fields.book_name | ellipsis }}</view>
									<view class="unique-book-description">{{ '作者很懒不想写任何书籍描述' | ellipsis }}</view>
								</view>
								<view v-if="20 == index" class="book_menu">
									<view class="title ">
										<view class="iconfont">&#xe629;</view>
										猜你喜欢
									</view>
									<navigator url="../list/index" open-type="switchTab"><view class="more">更多</view></navigator>
								</view>

								<view class="unique-book-item1" @click="goToChapter(i.pk, index)" v-if="((index - 20) % 7 === 0) & (index - 20 > 0)">
									<view><image mode="" lazy-load="" :src="i.fields.cover_url"></image></view>
									<view class="unique-book-name">{{ i.fields.book_name | ellipsis }}</view>
									<view class="unique-book-description">{{ '作者很懒不想写任何书籍描述' | ellipsis }}</view>
								</view>
								<view class="unique-book-item" @click="goToChapter(i.pk, index)" v-if="((index - 20) % 7 !== 0) & (index - 20 > 0)">
									<view><image lazy-load="" :src="i.fields.cover_url"></image></view>
									<view class="unique-book-name">{{ i.fields.book_name | ellipsis }}</view>
									<view class="unique-book-description">{{ '作者很懒不想写任何书籍描述' | ellipsis }}</view>
								</view>
							</block>
						</view>
					</view>
				</scroll-view>
			</swiper-item>
		</swiper>
	</view>
</template>
<script>
import Nav from '@/layout/nav';
import Search from '@/pages/search/index';
export default {
	data() {
		return {
			navList: [{ name: '推荐', url: '' }, { name: '更新', url: '' }],
			navIndex: 0,
			menuIndex: 0,
			mobile: 120,
			nav: [
				{ name: '排行榜', icon: '\ue61b', url: '/pages/index/sort', color: 'red' },
				{ name: 'VIP专区', icon: '\ue60e', url: '/pages/index/vip', color: 'red' },
				{ name: '书单', icon: '\ue690', url: '/pages/index/guide', color: 'red' },
				{ name: '积分商城', icon: '\ue617', url: '/pages/index/shop', color: 'red' }
			],
			sex: 0,
			showSearch: false,
			bookList: [],
			scrollTop: 0,
			storeTop: 0,
			control: 0,
			page: 6,
			id: 12,

			coverList: [
				{
					model: 'app.bookmodel',
					pk: 65,
					fields: {
						book_name: '\u6697\u591c\u534f\u594f\u66f2',
						cover_url: 'https://oss.mkzcdn.com/comic/cover/20181206/5c0888b707906-600x800.jpg!cover-400',
						description:
							'\n\u3000\u3000\u6c38\u6052\u7684\u5bfb\u627e\uff0c\u5bf9\u6297\u751f\u547d\u7684\u77ed\u6682\u8f6e\u56de\uff0c\u4e3a\u7684\u662f\u4e94\u767e\u5e74\u524d\u4e0d\u80af\u9057\u5fd8\u7684\u627f\u8bfa\u3002\u5e73\u51e1\u5973\u5b69\u4e0e\u5438\u8840\u738b\u5b50\u7684\u5947\u5f02\u9082\u9005\uff0c\u8ff7\u7cca\u5973\u5b69\u7684\u5e73\u9759\u751f\u6d3b\u5c06\u4f1a\u53d1\u751f\u600e\u6837\u7684\u6539\u53d8\uff1f\u8fd9\u5f98\u5f8a\u5728\u9752\u6885\u7af9\u9a6c\u7684\u90bb\u5bb6\u7537\u5b69\u548c\u5438\u8840\u738b\u5b50\u4e4b\u95f4\u7684\u5e73\u51e1\u5973\u5b69\uff0c\u53c8\u5c06\u4f55\u53bb\u4f55\u4ece\uff1f\u3000\u3000\n500\u5e74\u524d\uff0c\u5438\u8840\u9b3c\u7231\u4e0a\u4e86\u4e00\u4e2a\u4eba\u7c7b\u7684\u5973\u5b69\uff0c\u4f46\u662f\u56e0\u4e3a\u751f\u547d\u5468\u671f\u4e0d\u540c\uff0c\u4eba\u7c7b\u7684\u5973\u5b69\u6700\u540e\u6b7b\u4e86\u3002\u60b2\u4f24\u7684\u5438\u8840\u9b3c\u4e0d\u60f3\u518d\u53d7\u6b64\u4f24\u75db\uff0c\u60f3\u8981\u56de\u590d\u4eba\u7c7b\u7684\u8eab\u4efd\u3002\u7ec8\u4e8e\u627e\u5230\u53d8\u56de\u4eba\u7684\u65b9\u6cd5\u2026\u2026\n\u6211\u4eec\u7684\u6545\u4e8b\u5219\u53d1\u751f\u5728500\u5e74\u540e\u7684\u73b0\u4ee3\u3002\u4e00\u4e2a\u666e\u901a\u7684\u5973\u5b69\u539f\u672c\u8fc7\u7740\u5e73\u6de1\u7684\u6bcf\u4e00\u5929\uff0c\u5374\u88ab\u4e00\u53ea\u5438\u8840\u9b3c\u6270\u4e71\u4e86\u5979\u539f\u672c\u5e73\u9759\u7684\u751f\u6d3b\u3002\u7c89\u7ea2\u7684\u6d6a\u6f2b\u7231\u60c5\u534f\u594f\u66f2\u5373\u5c06\u54cd\u8d77\uff01',
						last_chapter: null
					}
				},
				{
					model: 'app.bookmodel',
					pk: 70,
					fields: {
						book_name: '\u963fSA\u4e13\u7528',
						cover_url: 'https://oss.mkzcdn.com/comic/cover/20181206/5c0888b7348bf-600x800.jpg!cover-400',
						description:
							'\n\u521d\u4e00\u7537\u751f\u201c\u72d0\u201d\u548c\u5fc3\u4eea\u5973\u5b69\u201c\u963fsa\u201d\u7684\u7b2c\u4e00\u6b21\u7ea6\u4f1a\uff0c\u5374\u88ab\u53f2\u4e0a\u6700\u8131\u7ebf\u6700\u5e05\u6c14\u7684\u9ed1\u767d\u65e0\u5e38\u544a\u77e5\uff0c\u4ed6\u5df2\u7ecf\u6b7b\u4e86\uff01\uff01\uff01\u88ab\u6293\u5230\u9634\u68ee\u6050\u6016\u7684\u960e\u738b\u6bbf\uff0c\u4ed6\u8981\u600e\u4e48\u5151\u73b0\u81ea\u5df1\u7684\u8bfa\u8a00\u2026\u2026\u3000\u3000\u6d6a\u6f2b\u7231\u60c5\u5267\uff0c\u4e3a\u5b88\u62a4\u7231\u7684\u4eba\u800c\u590d\u6d3b\u7684\u7537\u4e3b\u89d2\u3002\u6700\u73cd\u60dc\u7684\u4eba\uff0c\u6700\u73cd\u8d35\u7684\u7231\u60c5\uff0c\u674e\u96f7\u96f7\u9996\u6b21\u5728MK\u53d1\u8868\u7684\u8fde\u8f7d\u4f5c\u54c1\uff0c\u6f14\u7ece\u771f\u6b63\u7684\uff1a\u6b7b\u4e86\u90fd\u8981\u7231\uff01',
						last_chapter: null
					}
				},
				{
					model: 'app.bookmodel',
					pk: 96,
					fields: {
						book_name: '\u6781\u54c1\u7f8e\u5c11\u5973',
						cover_url: 'https://oss.mkzcdn.com/comic/cover/20180718/5b4eafeeedeb2-599x798.jpg!cover-400',
						description:
							'\n\u7537\u4e3b\u89d2\u738b\u5f3a\u662f\u5b66\u6821\u6253\u67b6\u80fd\u624b\uff0c\u6df7\u4e16\u9b54\u738b\uff0c\u4f46\u4ed6\u8fd8\u6709\u4e00\u4e2a\u5f31\u70b9\uff0c\u6015\u8eab\u4e3a\u73ed\u957f\u7684\u70b9\u84dd\u3002\u4e00\u6b21\u5728\u5de5\u5730\u4e0e\u70b9\u84dd\u7684\u51b2\u7a81\u4e2d\uff0c\u738b\u5f3a\u56e0\u4e3a\u81ea\u5df1\u6316\u9f3b\u5c4e\u800c\u610f\u5916\u7838\u6b7b\uff08=V=\uff09\u2022\u2022\u2022\u4f46\u662f\u56e0\u4e3a\u4ed6\u5f39\u9f3b\u5c4e\u81ea\u6740\u7684\u5671\u5934\u6cbb\u597d\u4e86\u5927\u5929\u4f7f\u957f\u7684\u5fe7\u90c1\u75c7\u2022\u2022\u2022\u4e8e\u662f\u5927\u5929\u4f7f\u957f\u7ed9\u4ed6\u4e00\u6b21\u590d\u6d3b\u7684\u673a\u4f1a\u2022\u2022\u2022\uff0c\u56e0\u4e3a\u5929\u4f7f\u6ca1\u6234\u773c\u955c\u770b\u4e0d\u6e05\u695a\uff0c\u738b\u5f3a\u7684\u7075\u9b42\u610f\u5916\u8dd1\u8fdb\u4e86\u5973\u4e3b\u89d2\u70b9\u84dd\u7684\u8eab\u4f53\u91cc\u2022\u53ef\u601c\u7684\u70b9\u84dd\u4fbf\u9644\u8eab\u5728\u4e00\u4e2a\u80cc\u5305\u4e0a\u9762\u2022\u2022\u738b\u5f3a\u88ab\u544a\u77e5\u5fc5\u987b\u7528\u70b9\u84dd\u7684\u8eab\u4f53\u5bfb\u627e\u5230\u4e00\u4efd\u771f\u7231\u624d\u53ef\u4ee5\u6062\u590d\u7537\u513f\u8eab\u3002\u4e3a\u4e86\u6062\u590d\u7537\u513f\u8eab\u2022\u2022\u2022\u4ed6\u5f00\u59cb\u4e86\u5168\u65b0\u7684\u751f\u6d3b',
						last_chapter: null
					}
				}
			]
		};
	},

	components: {
		'v-nav': Nav,
		'v-search': Search
	},
	filters: {
		ellipsis(str) {
			if (!str) return '';
			if (str.length > 6) {
				return str.slice(0, 6) + '...';
			}
			return str;
		}
	},
	methods: {
		tabChange(e) {
			this.navIndex = e.detail.current;
		},
		getData() {
			uni.request({
				url: this.$weburl + 'showBooklist/' + this.id + '/' + (this.id + this.page),
				success: res => {
					this.bookList = this.bookList.concat(res.data);
					this.id += this.page;
				}
			});
		},
		setShowsearch() {
			uni.hideTabBar({});
			uni.navigateTo({
				url: '../search/index'
			});
		},
		setMenuindex(index) {
			this.menuIndex = index;
			uni.showToast({
				icon: 'none',
				title: '功能暂停使用。。。'
			});
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
		
		
	}

	,
	onLoad() {
		
		uni.request({
			url: this.$weburl + 'showBooklist/0/12',
			data: {},
			header: {},
			success: res => {
				this.bookList = res.data;
				this.coverList = [];
				for (var i = 0; i < 4; i++) {
					this.coverList.push(res.data[i]);
				}
			}
		});
	},

	onPageScroll(e) {
		this.scrollTop = e.scrollTop;
		//手势下滑
		if (this.storeTop >= e.scrollTop) {
			if (this.control == 1) {
				uni.showTabBar({});
				uni.showTabBarRedDot({
					index: 3
				});
				this.control = 0;
			}
		}
		//手势上滑
		else {
			if (this.control == 0) {
				uni.hideTabBar({});
				this.control++;
			}
		}
		this.storeTop = e.scrollTop;
	}
};
</script>
<style scoped lang="scss">
.index_top_nav {
	background: rgba($color: #ffffff, $alpha: 1);
	display: flex;
	justify-content: space-between;
	align-items: center;
	position: fixed;
	top: 0;
	left: 0;
	width: 750rpx;
	color: white;
	height: 80rpx;
	font-size: 20upx;
	z-index: 100;
	color: black;
	.index_top_nav_item {
		display: flex;
		align-content: center;
		align-items: center;
		.control {
			margin-left: -15upx;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-content: center;
			text-align: center;
			font-weight: bolder;
		}
	}
}

.fixd_top_nav {
	//小程序添加
	// padding-top: 100rpx;
	background: #ffffff;

	display: flex;
	justify-content: space-between;
	align-items: center;
	position: fixed;
	top: 0;
	left: 0;
	width: 750upx;
	color: black;
	height: 80upx;
	font-size: 20upx;
	z-index: 100;

	.index_top_nav_item {
		display: flex;
		align-content: center;
		align-items: center;
		.control {
			margin-left: -15upx;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-content: center;
			text-align: center;
			font-weight: bolder;
		}
	}
}
.menu_list {
	padding-top: 20upx;
	padding-bottom: 20upx;
	display: flex;
	justify-content: center;
	align-items: center;
	width: 750upx;
	background: #ffffff;
	height: 120upx;
	font-size: 20upx;
	box-shadow: 2rpx 3rpx 3rpx rgba(0, 0, 0, 0.06);
	.menu_item {
		width: 187.5upx;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 120upx;
		.control {
			background-color: #ffffff;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-content: center;
			text-align: center;
			font-size: 30rpx;
		}
	}
}
.common {
	padding-bottom: 100rpx;
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 750rpx;
	.book_menu {
		width: 700rpx;
		display: flex;
		justify-content: space-between;
		padding: 20rpx 0;
		align-items: center;
		.title {
			font-size: 35rpx;
			font-weight: bold;
			display: flex;
			justify-content: space-between;
			align-items: center;
		}
		.iconfont {
			margin-right: 15rpx;
			color: orange;
			font-size: 30rpx;
		}
		.more {
			font-size: 20rpx;
		}
	}
	.book_list {
		width: 700rpx;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;

		image {
			width: 340rpx;
			height: 200rpx;
			border-radius: 20rpx;
		}
		.book_name {
			font-size: 30rpx;
			padding: 10rpx 0rpx;
			font-weight: bold;
		}
		.book-description {
			font-size: 10rpx;
			padding: 10rpx 0rpx;
			color: #c1c1c1;
			padding-bottom: 30rpx;
		}
		.unique-book-item1 {
			display: flex;
			flex-direction: column;
			align-content: center;
			margin: 0 auto;
			image {
				border-radius: 15rpx;
				width: 700rpx;
				height: 400rpx;
			}
		}
		.unique-book-item-last {
			image {
				border-radius: 15rpx;
				width: 700rpx;
				height: 250rpx;
			}
		}
		.unique-book-item {
			image {
				border-radius: 15rpx;
				width: 200rpx;
				height: 270rpx;
			}
		}
		.unique-book-name {
			font-size: 30rpx;
			padding: 10rpx 0rpx;
			font-weight: bold;
		}
		.unique-book-description {
			font-size: 10rpx;
			padding: 10rpx 0rpx;
			color: #c1c1c1;
			padding-bottom: 30rpx;
		}
	}
}
</style>
