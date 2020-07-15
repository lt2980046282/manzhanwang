<template>
	<view>
		<view class="username_list">
			<text class="username_item">用户名只能修改一次，请谨慎修改</text>
			<input  class="username_item" :value="username" />
			<button @click="submit" class="username_item">完成</button>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			
		};
	},
	onLoad() {
		uni.getStorage({
			key: 'username',
			success: res => {
				this.username = res.data;
			}
		});
	},
	props: {
		username:{
			type: String,
			default: ""
		},
	},
	methods:{
		
		submit(){
			
			uni.request({
				url:''
			})
			uni.redirectTo({
				url:'info'
			})
		}
	}
};
</script>

<style lang="scss">
	.username_list{
		font-size: 20rpx;
		padding-top: 30rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		text{
			display: flex;
			justify-content: flex-start;
		}
		input{
			border:  #C0C0C0 solid 2rpx;
			border-radius: 50rpx;
			width: 580rpx;
			height: 80rpx;
			margin-top: 20rpx;
			padding-left: 20rpx;
		}
		button{
			margin-top: 30rpx;
			background: #ff0000;
			font-size: 30rpx;
			font-weight: bold;
			color: #FFFFFF;
			width: 600rpx;
			height: 80rpx;
			border-radius: 50rpx;
			display: flex;
			align-items: center;
			justify-content: center;
		}
		
	}
page{
	background: #FFFFFF;
}
</style>
