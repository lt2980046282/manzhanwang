<template>
	<view>
		<view class="common">
			<view class="nav">
				<view class="nav-list">
					<view class="iconfont" @click="back">&#xe606;</view>
					<view class="nav-item">
						<view @click="setNav(index)" v-for="(i,index) in menuList" :key=index class="nav-title" :style="{color:index==current?'orange':''}">{{i}}</view>
						
					</view>
					<view class="iconfont"></view>
				</view>
			</view>
		</view>
		<swiper style="height: 100vh;" :current="current" @change="tabChange">
			<swiper-item v-for='i in 2' :key=i style="height: 100vh;">
				<scroll-view style="height: 100vh;" scroll-y="">
					<view class="common">
						<view class="control">
							<view v-for="(i, index) in bookList" :key="index" class="guide-list">
								<view class="guide-item">
									<image mode="aspectFill" :src="i.fields.cover_url"></image>
									<view class="book-name">{{ i.fields.book_name }}</view>
									<view class="book-num">10本</view>
								</view>
							</view>
						</view>
					</view>
				</scroll-view>
			</swiper-item>
		</swiper>
	</view>
</template>

<script>
export default {
	data() {
		return {
			menuList: ['最火书单', '推荐书单'],
			current: 0,
			bookList: []
		};
	},
	methods: {
		onClickItem(e) {
			if (this.current !== e.currentIndex) {
				this.current = e.currentIndex;
			}
		},
		tabChange(e) {
			this.current = e.detail.current;
		},
		setNav(i) {
			this.current = i;
		},

		back() {
			uni.navigateBack({});
			uni.showTabBar({});
		}
	},

	onShow() {
		uni.request({
			url: this.$weburl + 'showBooklist/0/12',
			data: {},
			header: {},
			success: res => {
				this.bookList = res.data;
			}
		});
	}
};
</script>

<style lang="scss">
.common {
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 750rpx;

	.nav {
		.iconfont{
			color: orange;
		}
		position: fixed;
		width: 750rpx;
		display: flex;
		height: 80rpx;
		justify-content: center;
		align-items: center;
		box-shadow: 1rpx 1rpx 1rpx #e5e5e5;
		z-index: 20;
		background-color: #ffffff;
		.nav-list {
			width: 700rpx;
			display: flex;
			justify-content: space-between;
			align-content: center;
			.nav-item {
				font-size: 30rpx;
				font-weight: bold;
				display: flex;
				justify-content: space-between;
				.nav-title {
					padding: 0 20rpx;
				}
			}
		}
	}
}
.control {
	padding-top: 100rpx;
	width: 700rpx;
	display: flex;
	flex-wrap: wrap;
	justify-content: space-between;
	.guide-list {
		width: 340rpx;
		image {
			height: 200rpx;
			width: 340rpx;
			border-radius: 10rpx;
		}
		.book-name{
			font-size: 30rpx;
			padding: 10rpx 0rpx;
			font-weight: bold;
		}
		.book-num{
			font-size: 10rpx;
			padding: 10rpx 0rpx;
			color: #c1c1c1;
			padding-bottom: 30rpx;
		}
	}
}
</style>
