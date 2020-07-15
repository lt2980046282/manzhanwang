<template>
	<view class="page">
		<view class="user_list">
			<view style="background: #FFFFFF;">
				<navigator url="/pages/my/info">
					<view class="user_login_info">
						<view class="user_login_info_left">
							<view v-if="!islogin" class="iconfont">&#xe614;</view>
							<view v-else class="logining"><image :src="header"></image></view>
							<view v-if="!islogin" class="user_description">
								<view>点击头像登录呦</view>
								<view>登录后畅享更多的功能~</view>
							</view>
						</view>
						<view class="user_login_info_right">签到领奖励</view>
					</view>
				</navigator>
				
				<view class="user_bag">
					<view class="user_bag_item" v-for="(i, index) in bag" :key="index">
						<view>{{ i.value }}</view>
						<view>{{ i.name }}</view>
					</view>
				</view>
			</view>
			<view class="user_item" v-for="(i, index) in nav" :key="index" @click="loginOut(index)" v-if="islogin && index==2 || index<2">
				<view class="user_item_left">
					<view style="display: flex;justify-content: center;align-items: center;line-height: 100rpx;vertical-align: middle;height: 100rpx;">
						<text class="iconfont">{{ i.icon }}</text>
						{{ i.name }}
					</view>
				</view>
				<view class="user_item_right"><view class="iconfont">&#xe658;</view></view>
			</view>
		</view>
	</view>
</template>
<script>
import Nav from '@/layout/nav';
export default {
	data() {
		return {
			nav: [
				{ name: '我的账户', icon: '\ue676', url: '/pages/index/index' },
				{ name: '我的消息', icon: '\ue89f', url: '/pages/list/index' },
				// { name: '任务中心', icon: '\ue608', url: '/pages/bookshelf/index' },
				// { name: '积分商城', icon: '\ue605', url: '/pages/my/index' },
				// { name: '兑换VIP', icon: '\ue65a', url: '/pages/my/index' },
				// { name: '意见反馈', icon: '\ue604', url: '/pages/my/index' },
				// { name: '请赐予我评分(p≧w≦q)', icon: '\ue628', url: '/pages/my/index' },
				// { name: '帮助中心', icon: '\ue70e', url: '/pages/my/index' },
				// { name: '我的设置', icon: '\ue65f', url: '/pages/my/index' },
				{ name: '退出登录', icon: '\ue65f', url: '/pages/my/index' }
			],
			bag: [],
			token: 'any',
			islogin: false,
			header: ''
		};
	},
	
	methods: {
		loginOut(i) {
			if(i==2){
				uni.setStorage({
					key: 'token',
					data: 'any',
					success: () => {
						this.token = 'any';
										this.bag = [{ name: '元宝', value: '-' }, { name: '月票', value: '-' }, { name: '积分', value: '-' }, { name: '阅读券', value: '-' }]
					}
				});
				uni.removeStorage({
					key: 'islogin',
					success: () => {
						this.islogin = false;
						
					}
				});
				uni.removeStorage({
					key:'bag'
				})
				uni.removeStorage({
					key: 'header',
					
				});
			}
		}
	},
	
	computed: {},
	onShow() {
		uni.hideTabBarRedDot({
			index:3
		})
		uni.getStorage({
			key: 'islogin',
			success: res => {
				
				this.islogin = res.data;
			},
			
		});
		uni.getStorage({
			key: 'token',
			success: res => {
				this.token = res.data;
			}
		});
		uni.getStorage({
			key:'bag',
			success: (res) => {
				this.bag = res.data
			},
			fail:()=>{
				this.bag = [{ name: '元宝', value: '-' }, { name: '月票', value: '-' }, { name: '积分', value: '-' }, { name: '阅读券', value: '-' }]
			}
		})
		uni.getStorage({
			key:'header',
			success:(res)=>{
				this.header = res.data
			},
			fail:()=>{
				uni.request({
					url: 'http://api.baititong.top:8000/getUserInfo/' + this.token,
					success: res => {
						if(this.islogin){
							const header = this.$weburl+res.data[0].fields.header;
							this.header = header
							this.bag = [{ name: '元宝', value: '99' }, { name: '月票', value: '44' }, { name: '积分', value: '12' }, { name: '阅读券', value: '123' }];
							uni.setStorage({
								key:'header',
								data:header,
							})
							uni.setStorage({
								key:'bag',
								data:[{ name: '元宝', value: '99' }, { name: '月票', value: '44' }, { name: '积分', value: '12' }, { name: '阅读券', value: '123' }],
							})
							
						}
					},
					
				});
			}
		})
		
	}
};
</script>
<style scoped lang="scss">
.user_list {
	display: flex;
	flex-direction: column;
	width: 750rpx;
	
	.user_login_info {
		background-color: to;
		background: linear-gradient(45deg,#FF8c00,#ff0000);
		display: flex;
		justify-content: space-between;

		align-items: center;
		.user_login_info_left {
			display: flex;
			justify-content: space-between;
			align-items: center;
			height: 200rpx;
			
			.iconfont {
				font-size: 100rpx;
				color: #ffffff;
				line-height: 200rpx;
				padding-left: 30rpx;
				padding-right: 30rpx;
			}
			.logining {
				border-radius: 20upx;
				padding-left: 40upx;
				padding-right: 20upx;
				margin-top: 20upx;
				image {
					border-radius: 100upx;
					width: 120upx;
					height: 120upx;
				}
			}
			.user_description {
				font-size: 25rpx;
				display: flex;
				flex-direction: column;
				color: #ffffff;
			}
		}
		.user_login_info_right {
			display: flex;
			align-items: center;
			font-size: 24rpx;
			background: #ffffff;
			height: 50rpx;
			border-radius: 50rpx 0rpx 0rpx 50rpx;
			padding-left: 40rpx;
			padding-right: 20rpx;
		}
	}
	.user_bag {
		font-size: 30rpx;
		color: #ffffff;
		padding: 15rpx;
		background: linear-gradient(135deg,#FF8c00,#ff0000);
		border-radius:  0rpx 0rpx  50% 50%;
		display: flex;
		justify-content: center;
		align-items: center;
		padding-bottom: 50rpx;
		font-size: 25rpx;
		.user_bag_item {
			width: 25%;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
		}
	}
	.user_item {
		background: #ffffff;
		padding-left: 30rpx;

		margin-bottom: 5rpx;
		display: flex;
		justify-content: space-between;
		align-items: center;
		display: flex;
		align-items: center;
		height: 150rpx;
		line-height: 150rp;
		.user_item_left {
			display: flex;
			align-items: center;
			line-height: 100rp;
	
			.iconfont {
				padding-right: 20rpx;
				display: flex;
				align-items: center;
				line-height: 100rp;
				color:#ff0000;
			}
		}
		.user_item_right {
			display: flex;
			align-items: center;
			height: 100rpx;
			line-height: 120px;
			.iconfont {
				font-size: 60rpx;
				color: #FF0000;
			}
		}
	}
}

.iconfont {
}
page{
	background: #E6E6E6;
}
</style>
