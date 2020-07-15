<template>
	<view>
		<view class="nav_list">
			<view class="nav_item" @click="setNav(index)" v-for="(i, index) in items" :key="index" :style="{ color: index == current ? '#ff0000' : '' }">{{ i }}</view>
		</view>
		<swiper style="height: 100vh;" :current="current" @change="tabChange">
			<swiper-item v-for="i in items.length" :key="i">
				<scroll-view style="height: 100vh" :lower-threshold="60" scroll-y>
					<view class="book_list">

						<view v-for="(i, index) in current==0?history:bookList" :key="index" class="book_item">
							<view class="book_left" @click="goToChapter(i.pk, index)">
								<view class="book_img">
									<image :src="i.fields.cover_url"></image>
								</view>
								<view class="book_info">
									<view class="book_name">{{i['fields']['book_name'] }}</view>
									<view class="book_reading">上次看到：{{ i['fields']['reading'] }}</view>
									<view>更新至：{{ bookList[0].index==0?'':i['fields']['last_chapter'] }}</view>
								</view>
							</view>
							<view class="book_read">
								<navigator :url="'../content/index?id=' + i.fields.book_read + '&book_id=' + i.pk">
									<view>续看</view>
								</navigator>
							</view>
						</view>
					</view>
				</scroll-view>
			</swiper-item>
		</swiper>
	</view>
</template>

<script>
	import Nav from '@/layout/nav.vue';
	export default {
		data() {
			return {
				items: ['历史', '收藏', '订购'],
				current: 0,
				bookList: [{
					pk: 0,
					fields: {
						cover_url: 'https://a1b2c3d4.alex-cosmetic.cn/2020/01/21/7f6298d8-b16e-485a-91b9-73a2babd6ed3.png',
						book_name: '灵剑尊',
						reading: '第234话 初到古剑城',
						last_chapter: '第234话 初到古剑城',
						book_read: '',
					},
					index: 0,
				}],
				token: 'any',
				history: []
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
				uni.setStorage({
					key: 'current',
					data: this.current
				})
			},
			setNav(i) {
				this.current = i;
				uni.setStorage({
					key: 'current',
					data: this.current
				})
			},
			goToChapter(i, index) {
				uni.navigateTo({
					url: '../chapter/index?id=' + i
				});
				uni.setStorage({
					key: 'cover' + i,
					data: this.i.fields.cover_url
				});
				uni.setStorage({
					key: 'book_name' + i,
					data: this.i.fields.book_name
				});
			},
			getData() {
				// uni.getStorage({
				// 	key:'bookShelfList',
				// 	success: (res) => {
				// 		this.bookList = res.data
				// 	},
				// 	fail:()=> {
				uni.request({
					url: this.$weburl + '/showBookShelfList/' + this.token,
					success: res => {
						if (res.data.code != 400) {

							uni.request({
								url: this.$weburl + '/showBookShelfListChapter/' + this.token,
								success: (res) => {
									for (var i in this.bookList) {
										this.bookList[i].fields.reading = res.data[i].reading
										this.bookList[i].fields.book_read = res.data[i].book_read
									}
								}
							})
							this.bookList = res.data;
							this.bookList[0].index =1
						} else {
							this.bookList = 0
						}
					},

				});
				// },

				// })

			}
		},

		onShow() {
			uni.getStorage({
				key: 'token',
				success: res => {
					this.token = res.data;
				}
			});
			this.getData()
			uni.getStorage({
				key: 'history',
				success: res => {
					this.history = res.data;

				}
			});
			uni.getStorage({
				key: 'current',
				success: (res) => {
					this.current = res.data
				}
			})
		},
		onLoad() {
			this.getData()
		}
	};
</script>

<style lang="scss">
	.nav_list {
		display: flex;
		justify-content: center;
		align-items: center;
		position: fixed;
		top: 0;
		left: 0;
		width: 750rpx;
		background: #ffffff;
		font-size: 20rpx;
		box-shadow: 0 0 3rpx 0 gray;
		z-index: 100;
		font-weight: bold;

		.nav_item {
			width: 250rpx;
			display: flex;
			justify-content: center;
			align-items: center;
			height: 120rpx;
			font-size: 35rpx;
		}
	}

	.book_list {
		padding-top: 120rpx;

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
