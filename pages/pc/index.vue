<template>
	<view class="page">
		<view class="header">
			<view class="nav">
				<image class="logo" src="../../static/images/pic_nav_logo.png"></image>
				<view v-for="i in navList" :key="i" class="nav-item"><text>{{ i }}</text></view>

				<view class="search">
					<input class="search-input" placeholder="斗破苍穹" ></input>
					<button class="search-button">搜索</button>
				</view>
				<view class="nav-item" v-for="i in menuList" :key="i">{{ i }}</view>

				<image class="user" src="@/static/images/pic_login_defaulthead.png" />
			</view>
		</view>
		<view class="common">
			<view class="banner">
				<view class="banner-left">
					<swiper style="height: 170rpx;width: 250rpx;" autoplay="" circular="" disable-touch="" indicator-active-color="white" indicator-dots="">
						<swiper-item v-for="i in 5" :key="i"><image src="https://oss.mkzcdn.com/image/20200102/5e0ddcdbdfa2d-750x500.jpg!banner-600-x" /></swiper-item>
					</swiper>
				</view>
				<view class="banner-right"><image v-for="i in banner1" :key="i" :src="i" /></view>
			</view>
			<view class="menu">
				
				<view v-for="i in menuList1" :key="i" class="menu-item">
					<view class="menu-item" v-if="i.title=='霸总'"><image src="../../static/icon/ic_index_class_lx.png"></image></view>
				<view class="menu-item" v-if="i.title=='连载'"><image src="https://static.mkzcdn.com/home/assets/images/icon/ic_index_class_jd.png"></image></view>
				<view class="menu-item" v-if="i.title=='最热'"><image src="https://static.mkzcdn.com/home/assets/images/icon/ic_index_class_rd.png?v=e599cd4"></image></view>
				<view class="menu-item" v-if="i.title=='免费'"><image src="https://static.mkzcdn.com/home/assets/images/icon/ic_index_class_ff.png"></image></view>
				<view class="menu-item" v-if="i.title=='全部分类'"><image src="https://static.mkzcdn.com/home/assets/images/icon/ic_home_class.png?v=e9df99b"></image></view>
				{{ i.title }}
				</view>
			</view>
			<view class="banner1">
				<view class="banner1-left">
					<view class="banner1-item">
						<image src="https://oss.mkzcdn.com/image/20200102/5e0ddb45645f8-750x422.jpg!cover-400-x"></image>
						<text class="title">斗罗大陆3龙王传说</text>
						<view class="author">作者：穆逢春 唐家三少</view>
						<view class="description">旷世之才，龙王之争。</view>
						<view class="rate">人气：19.67亿</view>
					</view>
				</view>
				<view class="banner1-right">
					<view class="banner1-item" v-for="i in banner2" :key="i">
						<image :src="i"></image>
						<view class="title">仙武帝尊</view>
						<view class="description">且看我置之死地而后生</view>
					</view>
				</view>
			</view>
			<view class="banner2"><image src="https://oss.mkzcdn.com/image/20200102/5e0ddf7ad3fe0-1500x140.jpg!banner-1500-x"></image></view>
			<view class="unique-menu">
				<view class="unique-menu-item">
					<view><image src="http://static.mkzcdn.com/home/assets/images/icon/ic_index_dj.png?v=c00ff63"></image></view>
					<view class="title">独家作品</view>
				</view>
				<view class="unique-menu-item">
					<view class="more">更多</view>
				
				</view>
			</view>
			<view class="banner3">
				<view class="banner3-item" v-for="i in 6" :key="i">
					<image src="https://oss.mkzcdn.com/comic/cover/20180817/5b76248a0e889-600x800.jpg!cover-400-x"></image>
					<view class="title">仙武帝尊</view>
					<view class="description">且看我置之死地而后生</view>
				</view>
			</view>
			<view class="unique-menu">
				<view class="unique-menu-item">
					<view><image src="http://static.mkzcdn.com/home/assets/images/icon/ic_index_ss.png?v=2781926"></image></view>
					<view class="title">上升最快</view>
				</view>
				<view class="unique-menu-item">
					<view>更多</view>
				</view>
			</view>
			<view class="banner3">
				<view class="banner3-item" v-for="i in 6" :key="i">
					<image src="https://oss.mkzcdn.com/comic/cover/20180817/5b76248a0e889-600x800.jpg!cover-400-x"></image>
					<view class="title">仙武帝尊</view>
					<view class="description">且看我置之死地而后生</view>
				</view>
			</view>
			<view class="unique-menu">
				<view class="unique-menu-item">
					<image src="http://static.mkzcdn.com/home/assets/images/icon/ic_index_xz.png?v=1f96a86"></image>

					<view class="title">新作尝鲜</view>
				</view>
				<view class="unique-menu-item">
					<view>更多</view>
				</view>
			</view>
			<view class="banner3">
				<view class="banner3-item" v-for="i in 6" :key="i"><image src="https://oss.mkzcdn.com/comic/cover/20180817/5b76248a0e889-600x800.jpg!cover-400-x"></image></view>
			</view>
			<view class="banner2"><image src="https://oss.mkzcdn.com/image/20200102/5e0ddf7ad3fe0-1500x140.jpg!banner-1500-x"></image></view>
			<view class="unique-menu">
				<view class="unique-menu-item">
					<view><image src="http://static.mkzcdn.com/home/assets/images/icon/ic_index_hz.png"></image></view>
					<view class="title">合作作品</view>
				</view>
				<view class="unique-menu-item">
					<view>更多</view>
				
				</view>
			</view>
			<view class="banner3">
				<view class="banner3-item" v-for="i in 6" :key="i">
					<image src="https://oss.mkzcdn.com/comic/cover/20180817/5b76248a0e889-600x800.jpg!cover-400-x"></image>
					<view class="title">仙武帝尊</view>
					<view class="description">且看我置之死地而后生</view>
				</view>
			</view>
			<view class="banner2"><image src="https://oss.mkzcdn.com/image/20200102/5e0ddf7ad3fe0-1500x140.jpg!banner-1500-x"></image></view>
			<view class="unique-menu">
				<view class="unique-menu-item">
					<view><image src="http://static.mkzcdn.com/home/assets/images/icon/ic_index_vip.png?v=a222a9a"></image></view>
					<view class="title">VIP专区</view>
				</view>
				<view class="unique-menu-item">
					<view>更多</view>
				
				</view>
			</view>
		</view>
	</view>
</template>
<script>
export default {
	data() {
		return {
			navList: ['首页', '更新', '排行', '分类', '专题', '小说'],
			menuList: ['消息', '历史', '收藏', '投稿', '下载APP'],
			menuList1: [
				
				{
					title: '霸总',
					url: '霸总'
				},
				{title: '玄幻',
					url: '玄幻'},
				{
					title: '修真',
					url: '修真'
				},
				{
					title: '恋爱',
					url: '恋爱'
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
				},
				{
					title: '最热',
					url: '最热'
				},
				{
					title: '最新',
					url: '最新'
				},
				{
					title: '免费',
					url: '免费'
				},
				{
					title: 'VIP免费',
					url: 'VIP免费'
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
					title: '全部分类',
					url: '全部分类'
				},
				
				
				
			],
			banner1:['https://oss.mkzcdn.com/image/20200102/5e0ddd4e40c83-900x300.jpg!banner-800-x','https://oss.mkzcdn.com/image/20200102/5e0ddda0d4e2f-750x500.jpg!banner-600-x','https://oss.mkzcdn.com/image/20200102/5e0dddbf47c75-750x500.jpg!banner-600-x','https://oss.mkzcdn.com/image/20200102/5e0ddde3b2287-750x500.jpg!banner-600-x','https://oss.mkzcdn.com/image/20200102/5e0dde9ad1933-750x500.jpg!banner-600-x','https://oss.mkzcdn.com/image/20200102/5e0ddd7dac6c5-900x300.jpg!banner-800-x'],
			banner2:['https://oss.mkzcdn.com/image/20191122/5dd7c391c1d35-750x422.jpg!cover-400-x','https://oss.mkzcdn.com/image/20200102/5e0dd3fd2f62f-750x422.jpg!cover-400','https://oss.mkzcdn.com/image/20200102/5e0dd5389f32b-750x422.jpg!cover-400-x','https://oss.mkzcdn.com/image/20200102/5e0dd29966a6f-750x422.jpg!cover-400-x','https://oss.mkzcdn.com/image/20200102/5e0dd5aaf33e4-750x422.jpg!cover-400-x','https://oss.mkzcdn.com/image/20200102/5e0dd66cc0bae-750x422.jpg!cover-400-x','https://oss.mkzcdn.com/image/20200102/5e0dd383b2b3a-750x422.jpg!cover-400','https://oss.mkzcdn.com/image/20200102/5e0dd312c25a3-750x422.jpg!cover-400-x'],
		};
	}
};
</script>
<style lang="scss">
page {
	padding: 0;
	margin: 0;
	font: 6rpx/1.33333 'PingFang SC', 'Lantinghei SC', 'Microsoft Yahei', 'Hiragino Sans GB', 'Microsoft Sans Serif', 'WenQuanYi Micro Hei', sans-serif;
}

.page {
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 750rpx;
	.header {
		width: 750rpx;
		border-bottom: 1rpx solid #e5e5e5;
		display: flex;
		align-items: center;
		justify-content: center;
		.nav {
			height: 30rpx;
			display: flex;
			align-items: center;
			width: 720rpx;
			justify-content: space-between;
			.logo {
				height: 23rpx;
				width: 60rpx;
			}
			.nav-item {
				font-size: 8rpx;
				width: 38rpx;
			}
			.user {
				height: 20rpx;
				width: 20rpx;
			}
			.search {
				display: flex;
				align-items: center;
				width: 170rpx;
				height: 20rpx;
				.search-input {
					height: 20rpx;
					border: 0.5rpx solid #ff620e;
					border-radius: 20rpx 0 0 20rpx;
					text-indent: 16rpx;
					width: 150rpx;
					
				}
				.search-button {
					color: white;
					display: flex;
					justify-content: center;
					align-items: center;
					height: 21rpx;
					width: 45rpx;
					border: 0.5rpx solid #ff620e;
					border-radius: 0 20rpx 20rpx 0;
					background: linear-gradient(135deg, #ff5b0f, #ff0f18);
					font-size: 8rpx;
				}
			}
		}
	}
}
.common {
	width: 720rpx;

	flex-wrap: wrap;
	.banner {
		display: flex;

		width: 720rpx;
		height: 170rpx;

		.banner-left {
			width: 240rpx;

			image {
				width: 240rpx;
				height: 170rpx;
			}
		}
		.banner-right {
			justify-content: space-between;
			display: flex;
			flex-wrap: wrap;
			margin-left: 2.5rpx;
			align-content: center;
			image:first-child,
			image:last-child {
				width: 235rpx;
				height: 84rpx;
			}
			image {
				margin-top: 1rpx;
				width: 120rpx;
				height: 84rpx;
			}
		}
	}
	.menu {
		display: flex;
		height: 30rpx;
		align-items: center;
		border-bottom: 1rpx solid #e5e5e5;
		width: 730rpx;
		justify-content: space-between;
		.menu-item {
			display: flex;
			
			font-size: 8rpx;
			image {
				margin-right: 5rpx;
				width: 10rpx;
				height: 10rpx;
			}
		}
		
	}
	.banner1 {
		margin-top: 5rpx;
		display: flex;
		width: 720rpx;
		.banner1-left {
			width: 240rpx;
			.banner1-item {
				image {
					width: 240rpx;
					height: 130rpx;
				}
				.author,
				.description,
				.rate,
				.title {
					font-size: 6rpx;
					color: #c1c1c1;
					padding: 1rpx;
				}
				.title {
					font-size: 10rpx;
					font-weight: bold;
					color: black;
				}
			}
		}
		.banner1-right {
			display: flex;
			flex-wrap: wrap;
			align-content: center;

			justify-content: space-between;
			margin-left: 2.5rpx;
			.banner1-item {
				display: flex;
				flex-direction: column;

				image {
					width: 115rpx;
					height: 80rpx;
				}
				.author,
				.description,
				.rate,
				.title {
					font-size: 6rpx;
					color: #c1c1c1;
					padding: 1rpx 0;
					overflow: hidden;
					white-space: nowrap;
					text-overflow: ellipsis;
					width: 100rpx;
				}
				.title {
					font-size: 10rpx;
					font-weight: bold;
					color: black;
				}
				.tag {
					position: absolute;
					left: 5px;
					bottom: 5px;
					padding: 0 5px;
					max-width: 130px;
					font-size: 12px;
					line-height: 22px;
					color: #fff;
					background: rgba(0, 0, 0, 0.65);
					z-index: 999;
					overflow: hidden;
					white-space: nowrap;
					text-overflow: ellipsis;
				}
			}
		}
	}
	,
	.banner2 {
		display: flex;
		padding-top: 10rpx;
		image {
			height: 70rpx;
			width: 720rpx;
		}
	}
	,
	.banner3 {
		display: flex;
		flex-wrap: wrap;
		width: 720rpx;
		justify-content: space-between;
		.banner3-item {
			display: flex;
			flex-direction: column;
			image {
				width: 115rpx;
				height: 170rpx;
			}
			.author,
			.description,
			.rate,
			.title {
				font-size: 6rpx;
				color: #c1c1c1;
				padding: 1rpx 0;
				overflow: hidden;
				white-space: nowrap;
				text-overflow: ellipsis;
				width: 100rpx;
			}
			.title {
				font-size: 10rpx;
				font-weight: bold;
				color: black;
				
			}
		}
	}
	,
	.unique-menu {
		display: flex;
		justify-content: space-between;
		width: 720rpx;
		height: 40rpx;
		.unique-menu-item {
			display: flex;
			align-items: center;
			height: 40rpx;
			justify-content: space-between;
			
			
			.title {
				font-size: 15rpx;
			}
			.iconfont{
				font-size: 10rpx;
				font-weight: normal;
			}
			image {
				width: 20rpx;
				height: 20rpx;
				padding-right: 2rpx;
			}
		}
	}
}
</style>
