<template>
	<view class="page">
		<view class="control" :style="{background:scrollTop >= 150?'#FFFFFF':''}">
			<view :class="scrollTop >= 150 ? 'fixd_top_nav' : 'top_nav'">
				<navigator open-type="navigateBack" :delta="2"><button class="back iconfont">&#xe606;</button></navigator>
				<view class="book_name">{{ scrollTop >= 150 ? book_name : '' }}</view>
			</view>
		</view>

		<view class="mask" :style="{ backgroundColor: scrollTop >= 150 ? '' : 'rgba(255,255,255,' + maskSize + ')', height: 250 + 'rpx' }"></view>
		<swiper style="z-index: 1;height: 400rpx;" :style="{ backgroundColor: scrollTop <= 150 ? 'rgba(255.255.255.0.1)' : '' }">
			<swiper-item><image lazy-load="true" style="width: 750rpx;" :src="cover"></image></swiper-item>
		</swiper>
		<view :class="scrollTop >= 150 ? 'menu_fixd' : 'menu'" style="z-index: 300;">
			<view class="nav_item" v-if="index == 0" @click="setNav(index)" v-for="(i, index) in items" :key="index" :style="{ color: index == current ? '#ff0000' : '' }">
				{{ i }}
			</view>
			<view class="nav_item" v-if="index == 1" @click="setNav(index)" v-for="(i, index) in items" :key="index" :style="{ color: index == current ? '#ff0000' : '' }">
				{{ i }}
				<view class="sort iconfont" @click="reversed">&#xe60d;{{ sortName }}</view>
			</view>
		</view>
		<swiper style="height: 100vh;z-index: 300;" @change="tabChange" :current="current">
			<swiper-item :key="0">
				<view class="description"><view class="author">作者简介：作者很懒什么都不写！</view></view>
			</swiper-item>
			<swiper-item :key="1">
				<scroll-view class="chapter_list" style="height: 100vh" :lower-threshold="600" scroll-y>
					<block v-for="(i, index) in chapterList" :key="i.pk" class="chapter_item">
						<view class="chapter_item" @click="goToContent(i)" :style="{ color: i.fields.chapter_order == currentChapter ? '#ff0000' : '' }">
							<view class="chapter_left"><image style="width: 300rpx;height: 200rpx" :src="i.fields.img_url" mode="aspectFill"></image></view>
							<view class="chapter_right">
								<view class="chapter_name">{{ i.fields.chapter_name }}</view>

								<view class="update_time">2002-12-21</view>
							</view>
						</view>
					</block>
				</scroll-view>
			</swiper-item>
		</swiper>
		<view class="chapter_nav">
			<view class="collection">
				<view @click="choiceBook()" :class="collectBook ? 'iconfont orange' : 'iconfont '">&#xe621;</view>
				<view>收藏</view>
			</view>
			<view class="comment">
				<view class="iconfont" style="font-size: 40rpx;">&#xe60b;</view>
				<view>评论</view>
			</view>
			<view v-if="currentChapter == -1" class="reading" @click="goToContent(chapterList[0])"><view>开始阅读</view></view>
			<view v-else class="reading" @click="goToContent(chapter)">
				<view>续看 {{ currentChapter }}话</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			items: ['详细', '目录'],
			current: 0,
			chapterList: [],
			book_id: 0,
			collectBook: false,
			scrollTop: 0,
			cover: '',
			token: 'any',
			iscollect: 0,
			history: [],
			currentChapter: 0,
			book_name: '',
			sort: false,
			sortName: '',
			
			maskSize: 0,
			description: '',
			chapter: {}
		};
	},
	methods: {
		//选择菜单栏
		onClickItem(e) {
			if (this.current !== e.currentIndex) {
				this.current = e.currentIndex;
			}
		},
		//收藏书籍
		choiceBook() {
			if (this.token == 'any') {
				uni.showToast({
					icon: 'none',
					title: '请登录后再尝试'
				});
			} else {
				this.collectBook = this.collectBook ? false : true;
				this.iscollect = this.collectBook ? 1 : 0;
				this.goTocollectBook();
			}
		},
		//执行收藏
		goTocollectBook() {
			uni.setStorage({
				key: 'book' + this.book_id,
				data: this.collectBook
			});
			uni.request({
				url: 'http://api.baititong.top:8000/collectBook/' + this.book_id + '/' + this.token + '/' + this.iscollect
			});
		},
		//前往内容页
		goToContent(i) {
			uni.navigateTo({
				url: '../content/index?id=' + i.fields.chapter_order + '&book_id=' + this.book_id
			});

			uni.setStorage({
				key: 'currentChapter' + this.book_id,
				data: i.fields.chapter_order
			}),
				uni.getStorage({
					key: 'history',
					success: res => {
						this.history = res.data;
						var j = this.history.findIndex((value, index, arr) => {
							return value.pk == this.book_id;
						});

						if (j == -1) {
							this.history.push({
								pk: this.book_id,
								fields: {
									cover_url: this.cover,
									book_name: this.book_name,
									reading: i.fields.chapter_name,
									last_chapter: this.chapterList[this.chapterList.length - 1].fields.chapter_name,
									book_read: i.fields.chapter_order
								}
							});
						} else {
							this.history[j].fields.reading = i.fields.chapter_name;
							this.history[j].fields.book_read = i.fields.chapter_order;
							this.history[j].fields.last_chapter = this.chapterList[this.chapterList.length - 1].fields.chapter_name;
						}
					},
					fail: () => {
						this.history.push({
							pk: this.book_id,
							fields: {
								cover_url: this.cover,
								book_name: this.book_name,
								reading: i.fields.chapter_name,
								last_chapter: this.chapterList[this.chapterList.length - 1].fields.chapter_name,
								book_read: i.fields.chapter_order
							}
						});
					}
				});
			uni.setStorage({
				key: 'history',
				data: this.history
			});
		},
		reversed() {
			this.chapterList.reverse();
			uni.getStorage({
				key: 'currentChapter' + this.book_id,

				fail: () => {
					this.currentChapter = 1;
				}
			});
		},

		tabChange(e) {
			this.current = e.detail.current;
		},
		setNav(i) {
			this.current = i;
			console.log(i)
		}
	},

	onLoad(option) {
		this.book_id = option.id;
		//添加历史记录

		uni.getStorage({
			key: 'book_name' + option.id,
			success: res => {
				this.book_name = res.data;
			}
		});

		uni.getStorage({
			key: 'cover' + option.id,
			success: res => {
				this.cover = res.data;
			},
			fail: () => {
				uni.request({
					url: 'http://api.baititong.top:8000/getBook/' + option.id, //仅为示例，并非真实
					success: res => {
						this.cover = res.data[0].fields.cover_url;
						this.book_name = res.data[0].fields.book_name;
						this.description = res.data[0].description;
					}
				});
			}
		});
		uni.getStorage({
			key: 'token',
			success: res => {
				this.token = res.data;
			}
		});

		uni.request({
			url: 'http://api.baititong.top:8000/getCollectBook/' + option.id + '/' + this.token,
			success: res => {
				this.collectBook = res.data == 1 ? true : false;
			}
		});
		uni.request({
			url: 'http://api.baititong.top:8000/showChapterlist/' + this.book_id + '/' + this.token, //仅为示例，并非真实接口地址。
			success: res => {
				this.chapterList = res.data;
				const chapter = res.data.findIndex((value, i, arr) => {
					return value.fields.chapter_order == this.currentChapter;
				});
				this.chapter = res.data[chapter];
				uni.setStorage({
					key: 'chapterList' + this.book_id,
					data: res.data
				});
			}
		});
	},
	//滚动动、动画淡入
	onPageScroll(e) {
		this.scrollTop = e.scrollTop;
		var i = 1 / 170;
		var j = 400 / 170;
		this.maskSize = i * e.scrollTop;
		this.maskHeight = 400 - j * screenTop;
	},
	onShow() {
		uni.getStorage({
			key: 'history',
			success: res => {
				const i = res.data.findIndex((value, i, arr) => {
					return value.pk == this.book_id;
				});
				if (i == -1) {
					this.currentChapter = -1;
				} else {
					this.currentChapter = res.data[i].fields.book_read;
					console.log();
				}
			},
			fail: () => {
				this.currentChapter = -1;
			}
		});
	}
};
</script>

<style scoped lang="scss">
.control {
	position: fixed;
	display: flex;
	flex-direction: column;

	width: 750rpx;
	z-index: 300;
	justify-content: center;
	align-items: center;
	height: 120rpx;
	.top_nav {
		width: 740rpx;
		display: flex;
		align-items: center;
		button{
			background-color: rgba($color: #000000, $alpha: 0);
		}
		.iconfont {
			color: #ffffff;
			font-size: 40upx;
			
		}
	}
	.fixd_top_nav {
		width: 740rpx;
		display: flex;
		align-items: center;
		z-index: 300;
		button{
			background-color: rgba($color: #000000, $alpha: 0);
		}
		.book_name {
			color: red;
			font-weight: bold;
			margin: auto;
		}
		.iconfont {
			color: #ff0000;
			font-size: 40upx;
		}
	}
}

.mask {
	top: 0;
	left: 0;
	position: fixed;
	
	width: 750rpx;
	z-index: 102;
}

.menu_fixd {
	position: fixed;
	z-index: 300;
	width: 750rpx;
	height: 100rpx;
	display: flex;
	justify-content: center;
	align-items: center;
	background-color: #ffffff;
	box-shadow: 0 0 5rpx 0 #e6e6e6;
	margin-top:-290rpx ;
	.nav_item {
		width: 375rpx;
		display: flex;
		justify-content: center;
		.sort {
			padding-left: 30rpx;
			font-size: 30rpx;
			display: flex;
			align-items: center;
			color: #ff0000;
		}
	}
}
.menu {
	border-bottom: 2rpx solid #cccccc;
	display: flex;
	justify-content: center;
	width: 750rpx;
	padding: 20rpx 0;
	z-index: 300;
	border-radius: 20rpx 20rpx 0 0;
	background-color: #ffffff;

	padding: 30rpx 0;
	.nav_item {
		width: 375rpx;
		display: flex;
		justify-content: center;
		.sort {
			padding-left: 30rpx;
			font-size: 30rpx;
			display: flex;
			align-items: center;
			color: #ff0000;
		}
	}
}
.chapter_list {
	flex-direction: column;
	padding-bottom: 150rpx;
	background-color: #ffffff;
	.chapter_item {
		display: flex;
		padding: 20rpx;
		border-bottom: 1rpx solid #c0c0c0;

		.chapter_name {
			font-size: 32rpx;
			padding-left: 20rpx;
		}
		.update_time {
			padding-top: 50rpx;
			padding-left: 20rpx;
			font-size: 25rpx;
		}
	}
}

.author {
	padding: 20rpx;
	font-size: 28rpx;
}
.chapter_nav {
	position: fixed;
	display: flex;
	bottom: 0;
	left: 0;
	background: #ffffff;
	width: 750rpx;
	height: 100rpx;
	align-items: center;
	z-index: 100;
	.collection {
		width: 200rpx;
		font-size: 20rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		.iconfont {
			font-size: 40rpx;
		}
	}
	.comment {
		display: flex;
		flex-direction: column;
		width: 125rpx;
		font-size: 20rpx;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		justify-content: center;
	}
	.reading {
		background: linear-gradient(135deg, #ff8c00, #ff0000);
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 32rpx;
	}
}
.orange {
	color: #ff0000;
}
swiper-item {
	background-color: #ffffff;
}
page {
	background-color: rgba($color: #000000, $alpha: 0.1);
}
</style>
