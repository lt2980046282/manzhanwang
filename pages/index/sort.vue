<template>
	<view>
		<view class="sort-top-nav">
			<view class="top-nav">
				<view class="control">
					<view @click="back" class="iconfont back">&#xe606;</view>
					<view>排行榜</view>
					<view @click="setShowsearch" class="iconfont">&#xe60a;</view>
				</view>
			</view>
			<view class="top-menu">
				<view class="control">
					<view class="top-menu-item" @click="setNav(index)" v-for="(i, index) in menuList" :key="index" :style="{ color: index == current ? '#ff0000' : '' }">{{ i }}</view>
				</view>
			</view>
		</view>
		<swiper style="height: 100vh;" :current="current" @change="tabChange">
			<swiper-item v-for="i in menuList.length" :key="i">
				<scroll-view style="height: 100vh" :lower-threshold="60" scroll-y>
					<view class="book_list">
						<view v-for="(i, index) in bookList" :key="index" class="book_item">
							<view class="book_left" @click="goToChapter(i.pk, index)">
								<view class="book_img"><image :src="i.fields.cover_url"></image></view>
								<view class="book_info">
									<view class="book_name">{{ i['fields']['book_name'] }}</view>
									<view class="book_reading">佚名</view>
									<view class="book_reading">热血</view>
									<view>只有实力才能守护家人</view>
								</view>
							</view>
							<view class="book_read">
								<view>{{index+1}}</view>
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
			menuList: ['人气', '月票', '收藏', '独家', '新作', '上升'],
			current: 0,
			bookList: [
				{
					pk: 0,
					fields: {
						cover_url: 'https://a1b2c3d4.alex-cosmetic.cn/2020/01/21/7f6298d8-b16e-485a-91b9-73a2babd6ed3.png',
						book_name: '灵剑尊',
						reading: '第234话 初到古剑城',
						last_chapter: '第234话 初到古剑城'
					},
					index: 0
				}
			]
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
		goToChapter(i, index) {},
		setShowsearch() {
			uni.hideTabBar({});
			uni.navigateTo({
				url: '../search/index'
			});
		},
		back(){
			uni.navigateBack({
				
			})
			uni.showTabBar({
				
			})
		}
	},
	onLoad() {
		
	},
	onShow() {
		uni.getStorage({
			key: 'token',
			success: res => {
				this.token = res.data;
			}
		});
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
.sort-top-nav {
	position: fixed;
	z-index: 100;
	.top-nav {
		display: flex;
		width: 750rpx;
		height: 100rpx;
		justify-content: center;
		align-items: center;
		background-color: #FFFFFF;
		.control {
			display: flex;
			width: 700rpx;
			justify-content: space-between;
			.back {
				font-size: 45upx;
			}
			.iconfont {
				color: red;
			}
		}
	}
	.top-menu {
		display: flex;
		justify-content: center;
		height: 70rpx;
		background-color: #FFFFFF;
		width: 750rpx;
		.control {
			font-size: 35rpx;
			width: 700rpx;
			display: flex;
			justify-content: space-between;
		}
	}
}
.book_list {
	margin-top: 180rpx;
	.book_item {
		display: flex;
		align-items: center;
		justify-content: space-between;
		font-size: 25rpx;
		color: gray;
		box-shadow: 0 0 2rpx 0 gray;
		padding: 30rpx 0;
		height: 180rpx;
		.book_left {
			display: flex;
			align-items: center;
			.book_img {
				width: 150rpx;
				height: 200rpx;
				image {
					width: 150rpx;
					height: 200rpx;
				}
			}
			.book_info {
				padding-left: 30rpx;
				.book_name {
					padding-bottom: 10rpx;
					font-size: 30rpx;
					color: #000000;
				}
				.book_reading {
					padding-bottom: 10rpx;
				}
			}
		}

		.book_read {
			padding-right: 30rpx;
		}
	}
}
</style>
