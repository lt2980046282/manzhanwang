<template>
	<view>
		<view class="input-box">
			<view class="input-item">
			    <view class="input-label">手机号</view>
				<view class="input-body">
					<input v-model="phone" maxlength="11" type="number" style="margin-right: 160upx;" placeholder="请输入手机号" class="input" >
					<button :disabled="!isCanSendCode" class="btn-code"  @click="sendCode">{{sendMsg}}</button>
				</view>
			</view>
			<view class="input-item">
				<view class="input-label">密码</view>
				<view class="input-body">
					<input v-model="password" type="text" :password="isHidePassword?true:false" style="margin-right: 50upx;" placeholder="请输入密码" maxlength="20"  class="input" />
					<image @click="isHidePasswordClick" class="eye" :src="isHidePassword?'/static/img/attention.png':'/static/img/attention_forbid.png'"></image>
				</view>
			</view>
			<view class="input-item">
				<view class="input-label">验证码</view>
				<view class="input-body">
					<input placeholder="请输入验证码" type="number" v-model="code" maxlength="6" class="input">
				</view>
			</view>
		</view>
		<button class="button" @click="submit">注册</button>
	</view>
</template>

<script>
	let timer = '';
	import {checkPhone,checkPwd,checkCode} from "@/common/common.js"
	export default {
		data() {
			return {
				sendMsg:"发送验证码",
				isCanSendCode:true,
				isHidePassword:true,
				phone:"",
				password:"",
				code:""
			};
		},
		onLoad() {
		},
		methods: {
			isHidePasswordClick(){
				this.isHidePassword=!this.isHidePassword
			},
			setCodeInterval () {
				//设置验证码重新发送定时器
			    let time = 60;
			    clearInterval(timer);
			    timer = setInterval(() => {
			        time--;
			        this.isCanSendCode=false;
			        this.sendMsg=time + "s"
			        if (time <= 0) {
			            this.isCanSendCode=true;
			            this.sendMsg="重新获取";
			            clearInterval(timer);
			        }
			    }, 1000)
			},
			clearCodeInterval(){
			    clearInterval(timer);
			    this.codemsg="获取验证码";
			},
			sendCode () {
				//发送验证码
			    if (!checkPhone(this.phone)) {
			        return
			    }
			    this.setCodeInterval();
				uni.request({
					url: 'http://api.baititong.top:8000/sendSms/'+this.phone,
					success: (res) => {
						if(res.data.code===2){
							uni.showToast({
								icon:'none',
								title:'发送成功',
							})
						}
					}
				})
			},
			submit() {
				if(!checkPhone(this.phone)){
					return;
				};
				if(!checkPwd(this.password)){
					return;
				};
				if(!checkCode(this.code)){
					return;
				};
				/*
				* 注册逻辑
				*/
				this.$store.commit('update',['isLogin',true]);
				uni.request({
					url:'http://api.baititong.top:8000/register/'+this.phone+'/'+this.password+'/'+this.code,
					success: (res) => {
						uni.showToast({
							title:res.data.name
						})
						if(res.data.code===101){
							uni.reLaunch({
								url:'/pages/my/index'
							})
						}
					}
				})
				
			}
		}
	}
</script>

<style>
	uni-button{
		background: linear-gradient(45deg,#ff0000,#FF8c00);
	}
</style>
