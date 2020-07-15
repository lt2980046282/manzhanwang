<template>
	<view class="page">
		<view :class="isShow ? 'control' : 'hide'">
			<view :class="isShow ? 'top_nav' : 'hide'">
				<view @click="back" class="back iconfont">&#xe606;</view>
				<view class="book_name">{{ chapter_name }}</view>
				
			</view>
		</view>
		<view v-if="1 == this.chapter_id" style="font-size: 28rpx;display: flex;justify-content: center;width: 750rpx;height: 100rpx;align-items: center;background: #FFFFFF;">
			已经是第一页了
		</view>
		<view class="count">
			{{ currentPhoto.fields.pic_order }}/{{ currentPhoto.fields.sum }} {{ currentPhoto.fields.chapter_name }}
		</view>

		<view v-if="isShow" :class="isShow ? 'nav' : 'hide_nav'">
			<button style="color: #FFFFFF;"></button>
			<button @click="backTobook()" style="color: #FFFFFF;">目录</button>
			<button style="color: #FFFFFF;"></button>
		</view>

		<image @click="setShow()" class="content_item" v-for="i in photoList" :key="i.pk" mode="widthFix" :src="i.fields.img_url" style="margin-top: -1px;"></image>
	</view>
</template>

<script>
export default {
	data() {
		return {
			photoList: [],
			chapter_id: 0,
			book_id: 0,
			isShow: true,
			token: '',
			currentChapter: 0,
			count: 1,
			islogin: false,
			timer: '',

			chapter_name: '',

			chapterList: [],
			history: [],
			currentPhoto: {
				fields: {}
			},
			
		};
	},
	components: {},
	onLoad(option) {
		//获取用户口令
		
		uni.getStorage({
			key: 'token',
			success: res => {
				this.token = res.data;
			}
		});
		
		//获取当前章节id
		uni.getStorage({
			key: 'chapter' + option.book_id,
			success: res => {
				this.currentChapter = res.data;
			}
		});
		this.chapter_id = option.id;
		this.book_id = option.book_id;
		//获取本地章节列表
		uni.getStorage({
			key: 'chapterList' + option.book_id,
			success: res1 => {
				this.chapterList = res1.data;
				this.chapter_name = res1.data[this.chapter_id - 1].fields.chapter_name;
				uni.request({
					url: this.$weburl+'showPhotolist/' + res1.data[this.chapter_id - 1].pk + '/' + this.token, //仅为示例，并非真实接口地址。
					data: {},
					header: {},
					success: res => {
						uni.request({
							url:this.$weburl+'uploadpProgress/' + this.chapter_id +'/'+option.book_id+'/'+this.chapter_name + '/' + this.token, 
							
						})
						var data = res.data;
						var sum = res.data.length;
				
						for (var i in data) {
							data[i].fields.chapter_name = this.chapter_name;
							data[i].fields.sum = sum;
				
							this.photoList.push(data[i]);
						}
						this.currentPhoto.fields.pic_order = 1;
						this.currentPhoto.fields.sum = sum;
						this.currentPhoto.fields.chapter_name = this.chapter_name;
					}
				});
			}
		});
		
		//判断是否已登录
		uni.getStorage({
			key: 'islogin',
			success: res => {
				this.islogin = res.data;
			},
			fail: res => {
				uni.showToast({
					icon:'none',
					title:'请登录后在进行尝试！',
					
					success() {
						setTimeout(function() {uni.redirectTo({
							url: '../user/login'
						});}, 1000);
						
					}
				})
				
			}
		});
		//获取本地历史纪录
		uni.getStorage({
			key: 'history',
			success: res => {
				this.history = res.data;
				const i = this.history.findIndex((value, i, arr) => {
					return value.pk == this.book_id;
				});
				uni.setStorage({
					key:'index',
					data:i,
				})
			}
		});
	},
	methods: {
		//获取当前时间
		getTime() {
			var date = new Date(),
				hour = date.getHours() < 10 ? '0' + date.getHours() : date.getHours(),
				minute = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes(),
				second = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds();

			var timer = hour + ':' + minute + ':' + second;
			this.timer = timer;
		},
		
		getChapter(i) {
			if (i >= 'mix') {
				++this.chapter_id;
				++this.currentChapter;
			} else {
				--this.chapter_id;
				--this.currentChapter;
			}
			uni.setStorage({
				key: 'chapter' + this.book_id,
				data: this.currentChapter
			});

			if (this.chapter_id > this.max_chapter_num) {
				uni.showToast({
					title: '没有更多'
				});
				this.min_chapter_num++;
			} else if (this.chapter_id < this.min_chapter_num) {
				uni.showToast({
					title: '没有更多'
				});
				this.min_chapter_num--;
			} else {
				uni.navigateTo({
					url: '../content/index?id=' + this.chapter_id + '&book_id=' + this.book_id
				});
			}
		},
		//退回目录页
		backTobook() {
			uni.navigateTo({
				url: '../chapter/index?id=' + this.book_id
			});
		},
		
		getData() {
			this.chapter_id++;
			uni.request({
				url: 'http://api.baititong.top:8000/showPhotolist/' + this.chapter_id + '/' + this.token, //仅为示例，并非真实接口地址。
				data: {},
				header: {},
				success: res => {
					this.photoList.push(res.data);
				}
			});
		},
		//导航条控制器
		setShow() {
			uni.getNetworkType({
				success: function(res) {
					this.netType = res.networkType;
				}
			});
			if (this.isShow) {
				this.isShow = false;
			} else {
				this.isShow = true;
			}
		},
		back() {
			uni.navigateBack({
				
			});
		}
	},
	//监听章节数据
	onPageScroll(e) {
		if (this.storeTop != e.scrollTop) {
			this.isShow = false;
		}

		var length = this.photoList.length;
		var a = 0;
		uni.createSelectorQuery()
			.selectAll('.content_item')
			.boundingClientRect(res => {
				var min = Math.abs(res[0].top);

				for (var i = 0; i < length; i++) {
					if (Math.abs(res[i].top) < min) {
						min = Math.abs(res[i].top);

						a = i;
					}
				}

				this.currentPhoto = this.photoList[a];
			})
			.exec();

		this.storeTop = e.scrollTop;
	},
	//到达底部加载数据
	onReachBottom() {
		this.chapter_id++;
		this.currentChapter++;
			uni.setStorage({
				key: 'currentChapter' + this.book_id,
				data: this.currentChapter
			});
		uni.request({
			url: this.$weburl+'showPhotolist/' + this.chapterList[this.chapter_id - 1].pk + '/' + this.token, //仅为示例，并非真实接口地址。
			success: res => {
				if (res.data) {
					this.chapter_name = this.chapterList[this.chapter_id - 1].fields.chapter_name;

					var data = res.data;
					var sum = res.data.length;
					for (var i in data) {
						data[i].fields.chapter_name = this.chapter_name;
						data[i].fields.sum = sum;
						this.photoList.push(data[i]);
						
					}

					this.currentChapterlength = res.data.length;
					this.oneChapter = res.data.length;

					this.currentChapterlength = res.data.length;
					this.count = 1;	
					uni.getStorage({
						key:'index',
						success: (res) => {
							this.history[res.data].fields.reading = this.chapterList[this.chapter_id - 1].fields.chapter_name;
							this.history[res.data].fields.book_read = this.chapter_id;
						}
					})

					uni.setStorage({
						key: 'history',
						data: this.history
					});
				} 
			}
		});
	uni.request({
		url:this.$weburl+'uploadpProgress/' + this.chapter_id +'/'+this.book_id+'/'+this.chapter_name + '/' + this.token, 
		
	})
	},
	

};
</script>

<style style="sass" lang="scss">
.control{
	position: fixed;
	display: flex;
	flex-direction: column;
	z-index: 10;
	width: 750rpx;
	background-color: rgba($color: #000000, $alpha: 0.85);
	justify-content: center;
	align-items: center;
	height: 100rpx;
	.top_nav {
		width: 700rpx;
		display: flex;
		
		align-items: center;
		.book_name {
			color: white;
			font-weight: bold;
			margin: auto;
		}
		.iconfont {
			color: #ffffff;
			font-size: 45upx;
		}
	}
}
.count {
	position: fixed;
	bottom: 0;
	right: 0;
	z-index: 50;
	background: rgba($color: #000000, $alpha: 0.4);
	border-radius: 50rpx #000000;
	color: white;
	display: flex;

	padding: 10rpx;
	font-size: 25rpx;
	padding-left: 30rpx;
	padding-right: 70rpx;
}
.nav {
	width: 750rpx;
	display: flex;
	position: fixed;
	left: 0;
	bottom: 0;
	background-color: rgba($color: #000000, $alpha: 0.85);
	box-shadow: 1upx #2c405a;
	z-index: 100;
	uni-button {
		background-color: rgba($color: #000000, $alpha: 0);
	}
}
uni-image {
	padding: 0;
	display: flex;
}
image {
	padding: 0;
	margin: 0;
	display: flex;
	width: 750upx;
	margin-top: -1upx;
}
.hide_nav {
	animation: hide 1s linear both;
	width: 750rpx;
	display: flex;
	position: fixed;
	left: 0;
	bottom: 0;
	background-color: rgba($color: #000000, $alpha: 0.85);
	box-shadow: 1upx #2c405a;
	z-index: 100;
	button {
		background-color: rgba($color: #000000, $alpha: 0.85);
	}
}
.hide {
	animation: hide 1s linear both;
	position: fixed;
	display: flex;
	flex-direction: column;
	z-index: 10;
	width: 750rpx;
	background-color: rgba($color: #000000, $alpha: 0.85);
	justify-content: center;
	align-items: center;
	height: 100rpx;
	.top_nav {
		width: 700rpx;
		display: flex;
		
		align-items: center;
		.book_name {
			color: white;
			font-weight: bold;
			margin: auto;
		}
		.iconfont {
			color: #ffffff;
			font-size: 45upx;
		}
	}
}
@keyframes hide {
	0% {
		opacity: 1;
	}
	100% {
		opacity: 0;
	}
}
</style>
