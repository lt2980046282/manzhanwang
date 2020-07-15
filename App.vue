<script>
import Vue from 'vue';
export default {
	onLaunch: function() {
	
		uni.getSystemInfo({
			success: function(e) {
				// #ifndef MP
				Vue.prototype.StatusBar = e.statusBarHeight;
				if (e.platform == 'android') {
					Vue.prototype.CustomBar = e.statusBarHeight + 50;
				} else {
					Vue.prototype.CustomBar = e.statusBarHeight + 45;
				}
				// #endif
				// #ifdef MP-WEIXIN
				Vue.prototype.StatusBar = e.statusBarHeight;
				let custom = wx.getMenuButtonBoundingClientRect();
				Vue.prototype.Custom = custom;
				Vue.prototype.CustomBar = custom.bottom + custom.top - e.statusBarHeight;
				// #endif
				// #ifdef MP-ALIPAY
				Vue.prototype.StatusBar = e.statusBarHeight;
				Vue.prototype.CustomBar = e.statusBarHeight + e.titleBarHeight;
				// #endif
			}
		});
	},
	onShow: function() {},
	onHide: function() {}
};
</script>

<style lang="scss">
/* 解决头条小程序组件内引入字体不生效的问题 */
@font-face {
	font-family: uniicons;
	src: url('/static/uni.ttf');
}
@font-face {
  font-family: 'iconfont';  /* project id 1525278 */
 
  src:url('static/iconfont/iconfont.ttf') format('truetype'),

}
.iconfont {
	font-family: "iconfont" !important;
	-webkit-text-stroke-width: 1.5rpx;
	vertical-align: middle;
	
}

button::after {
	border: none;
}
.input-box {
	padding: 50upx;
	font-size: 30upx;
	.input-item {
		display: flex;
		background: white;
		border-bottom: 1upx solid #eeeeee;
		line-height: 100upx;
		height: 100upx;
		.input-label {
			width: 150upx;
		}
		.input-body {
			position: relative;
			height: 100upx;
			width: calc(100% - 150upx);
			.input {
				line-height: 100upx;
				height: 100upx;
				position: relative;
				font-size: 28upx;
			}
			.eye {
				position: absolute;
				height: 50upx;
				width: 50upx;
				right: 0;
				top: 50%;
				transform: translateY(-50%);
			}
			.btn-code {
				position: absolute;
				right: 0upx;
				top: 50%;
				transform: translateY(-50%);
				background: none;
				color: #205592;
				width: 160upx;
				font-size: 24upx;
				box-sizing: border-box;
				text-align: right;
				padding: 0;
				height: 100upx;
				line-height: 100upx;
			}
		}
	}
	.select {
		padding-top: 40upx;
		display: flex;
		justify-content: space-between;
		color: #003b67;
	}
}
.button {
	margin: 0 30upx;
	background: #ff0000;
	border-radius: 50upx;
	line-height: 80upx;
	height: 80upx;
	color: white;
	font-size: 32upx;
}
.uni-tabbar {
	height: 100rpx;
	font-weight: bold;
}
.uni-page-head {
	background: linear-gradient(135deg, #ff8c00, #ff0000);
}
.uni-app{
	overflow: hidden;
}
</style>
