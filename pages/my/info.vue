<template>
	<view>
		<view class="top_nav">
			<navigator url="../my/index" open-type="switchTab"><view class="back iconfont">&#xe606;</view></navigator>
		</view>
		<view :class="currentClass" v-if="!isShow">
			<block v-for="(i, index) in menuList" :key="index">
				<button v-if="index === 0" class="info_item" @click="showLayout(0)">
					<view class="info_left">{{ i.name }}</view>
					<view class="info_right">
						<view class="logining"><image :src="i.img"></image></view>
						<view class="iconfont">&#xe658;</view>
					</view>
				</button>
				<button v-if="index !== 0" class="info_item" @click="showLayout(index)">
					<view class="info_left">{{ i.name }}</view>
					<view class="info_right">
						<view class="logining">{{ i.value }}</view>
						<view class="iconfont">&#xe658;</view>
					</view>
				</button>
				<!-- 遮盖层-->
				<view v-if="menuList[index].isShow" @click="showLayout(index)" class="mask"></view>
			</block>
		</view>
		<!-- 头像选择模块 -->
		<view class="header_list" v-if="menuList[0].isShow">
			<view class="header_item">
				点击上
				<avatar style="width: 0rpx;height: 0rpx;" selWidth="200px" selHeight="400upx" @upload="myUpload"></avatar>
				传
			</view>
			<view class="cancel" @click="showLayout(0)">取消</view>
		</view>
		<!-- 性别选择模块 -->
		<view class="sex_list" v-if="menuList[3].isShow">
			<view @click="setSex(0)" class="sex_item">男</view>
			<view @click="setSex(1)" class="sex_item">女</view>
			<view @click="setSex(2)" class="sex_item">保密</view>
			<view class="cancel" @click="showLayout(3)">取消</view>
		</view>
		<view v-if="menuList[1].isShow"><v-username :username="menuList[1].value"></v-username></view>
		<view v-if="menuList[2].isShow"><v-username :username="menuList[2].value"></v-username></view>
		<view v-if="menuList[6].isShow"><v-username :username="menuList[2].value"></v-username></view>
	</view>
</template>

<script>
import avatar from '@/components/yq-avatar/yq-avatar.vue';
import username from '@/pages/my/cag-username.vue';
export default {
	data() {
		return {
			menuList: [
				{ name: '头像', img: '', url: '', iconfont: '\ue658', method: '', img: '../../static/images/douyin/4.jpg', isShow: false },
				{ name: '用户名', img: '', url: '', iconfont: '\ue658', method: '', value: 'mmmaldalkdlladlaskdklas', isShow: false },
				{ name: '昵称', img: '', url: '', iconfont: '\ue658', method: '', value: 'mmmaldalkdlladlaskdklas', isShow: false },
				{ name: '性别', img: '', url: '', iconfont: '\ue658', method: '', value: '保密', isShow: false },
				{ name: '星座', img: '', url: '', iconfont: '\ue658', method: '', value: '选择出生日期，系统自动转化为星座', isShow: false },
				{ name: '领地', img: '', url: '', iconfont: '\ue658', method: '', value: '123', isShow: false },
				{ name: '设置密码', img: '', url: '', iconfont: '\ue658', method: '', value: '', isShow: false },
				{ name: '绑定手机', img: '', url: '', iconfont: '\ue658', method: '', value: '150****2903', isShow: false },
				{ name: '绑定邮箱', img: '', url: '', iconfont: '\ue658', method: '', value: '未绑定，可以在电脑端绑定邮箱', isShow: false },
				{ name: '绑定QQ', img: '', url: '', iconfont: '\ue658', method: '', value: '去绑定', isShow: false },
				{ name: '绑定微信', img: '', url: '', iconfont: '\ue658', method: '', value: '去绑定', isShow: false },
				{ name: '绑定微博', img: '', url: '', iconfont: '\ue658', method: '', value: '去绑定', isShow: false }
			],
			sex: 0,
			url: '../../static/logo.png',
			islogin: false,
			currentClass: 'info_list',
			isShow: false,
			token: 'any'
		};
	},
	methods: {
		//设置性别
		setSex(i) {
			this.sex = i;
			this.menuList[3].isShow = false;
			this.menuList[3].value = i === 0 ? '男' : i == 1 ? '女' : '保密';
		},
		//模拟动态绑定方法
		showLayout(key) {
			if ((key == 0) | (key == 3)) {
				this.menuList[key].isShow = this.menuList[key].isShow ? false : true;
			}
			if ((key == 1) | (key == 2) | (key == 6)) {
				this.menuList[key].isShow = true;
				this.currentClass = 'white';
				this.isShow = true;
			}
		},
		//图片裁剪上传功能
		myUpload(rsp) {
			this.url = rsp.path; //更新头像方式一
			//rsp.avatar.imgSrc = rsp.path; //更新头像方式二
			this.menuList[0].isShow = false;
			uni.uploadFile({
				url: 'http://api.baititong.top:8000/upLoadHeader/' + this.token, //仅为示例，非真实的接口地址
				filePath: rsp.path,
				name: 'avatar',
				success: res => {
					const data = JSON.parse(res.data);
					if (data.code == 501) {
						this.menuList[0].img = this.$weburl + data.url;
						uni.setStorage({
							key: 'header',
							data: this.menuList[0].img
						});
					}
				}
			});
		}
	},
	onLoad() {
		//判断用户是否已登录
		uni.getStorage({
			key: 'token',
			success: res => {
				this.token = res.data;
			}
		});
		uni.getStorage({
			key: 'islogin',
			success: res => {
				this.islogin = res.data;
				uni.request({
					url: 'http://api.baititong.top:8000/getUserInfo/' + this.token,
					success: res => {
						if (this.islogin) {
							const header = this.$weburl + res.data[0].fields.header;
							this.menuList[0].img = this.$weburl + res.data[0].fields.header;
							uni.setStorage({
								key: 'header',
								data: header
							});
						}
					}
				});
			},
			fail: () => {
				this.islogin = false;
				uni.redirectTo({
					url: '../user/login'
				});
			}
		});
		// 保存token
	},
	components: {
		avatar,
		'v-username': username
	},
	onShow() {
		uni.getStorage({
			key: 'header',
			success: res => {
				this.menuList[0].img = res.data;
			},
			fail: () => {
				if (this.islogin) {
					uni.request({
						url: 'http://api.baititong.top:8000/getUserInfo/' + this.token,
						success: res => {
							this.menuList[0].img = this.$weburl + res.data[0].fields.header;
							uni.setStorage({
								key: 'header',
								data: this.menuList[0].img
							});
						}
					});
				}
			}
		});
	}
};
</script>

<style lang="scss">
.top_nav {
	display: flex;
	width: 730rpx;
	padding-left: 20rpx;
	align-items: center;
	background: linear-gradient(135deg, #ff8c00, #ff0000);
	height: 100rpx;
	.iconfont {
		color: #ffffff;
		font-size: 45upx;
	}
}
.info_list {
	background: #cccccc;
	.info_item {
		background: #ffffff;
		padding-left: 20upx;
		width: 750upx;
		margin-top: 1upx;
		display: flex;
		justify-content: space-between;
		align-items: center;
		height: 100upx;
		border-radius: 0;

		.info_left {
			font-size: 30upx;
		}
		.info_right {
			display: flex;
			align-items: center;
			height: 100upx;
			line-height: 100rpx;
			.logining {
				font-size: 30upx;
				border-radius: 20upx;
				padding-left: 40upx;
				padding-right: 20upx;
				display: flex;
				align-items: center;
				image {
					border-radius: 100upx;
					width: 70upx;
					height: 70upx;
				}
			}
			.iconfont {
				font-size: 60upx;
			}
		}
	}
}
// 遮盖层
.mask {
	background: rgba(0, 0, 0, 0.3);
	height: 100vh;
	width: 750rpx;
	z-index: 100;
	position: fixed;
	top: 0;
	left: 0;
}
// 性别选择模块
.sex_list {
	display: flex;
	flex-direction: column;
	align-items: center;
	position: fixed;
	bottom: 0;
	left: 0;
	z-index: 120;
	background: #cccccc;
	.sex_item {
		background: #ffffff;
		width: 710rpx;
		display: flex;
		justify-content: center;
		padding: 22rpx;
		margin-bottom: 1rpx;
	}
	.cancel {
		margin-top: 20rpx;
		background: #ffffff;
		width: 710rpx;
		display: flex;
		justify-content: center;
		padding: 22rpx;
	}
}
.header_list {
	background: #cccc;
	display: flex;
	flex-direction: column;
	align-items: center;
	position: fixed;
	bottom: 0;
	left: 0;
	z-index: 120;
	.header_item {
		background: #ffffff;
		width: 710rpx;
		display: flex;
		justify-content: center;
		padding: 22rpx;
		margin-bottom: 1rpx;
	}
	.cancel {
		margin-top: 20rpx;
		background: #ffffff;
		width: 710rpx;
		display: flex;
		justify-content: center;
		padding: 22rpx;
	}
}
.white {
	background: #ffffff;
}
</style>
