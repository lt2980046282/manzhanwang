<template>
	<view>
		<view class="sort-top-nav">
			<view class="top-nav">
				<view class="control">
					<navigator open-type="navigateBack"><view class="iconfont back">&#xe606;</view></navigator>
					<view>漫栈网 .VIP</view>
					<view class="iconfont">&#xe60a;</view>
				</view>
			</view>
		</view>
		<view class="content">
			<swiper style="width: 750rpx;height: 400rpx;" indicator-dots="" indicator-active-color="red">
				<swiper-item style="display: flex;justify-content: center;"><image style="width: 730rpx;" src="../../static/images/douyin/0.jpg"></image></swiper-item>
				<swiper-item style="display: flex;justify-content: center;"><image style="width: 730rpx;" src="../../static/images/douyin/0.jpg"></image></swiper-item>
			</swiper>
		</view>
		<view class="common">
			<view class="tip">
				<view class="tip-icon">续费VIP，特权永不断</view>
			</view>
			<view class="book_list">
				<view class="book_item" v-for="(i, index) in bookList" :key="index" @click="goToChapter(i.pk, index)">
					<view class="control">
						<view><image lazy-load="" mode="aspectFill" :src="i.fields.cover_url"></image></view>
						<view class="book_name">{{ i.fields.book_name }}</view>
						<view class="chapter_name">{{ i.fields.last_chapter }}</view>
					</view>
				</view>
			</view>
			<view class="update-book-list">
				<view class="update-book-list-title" ><view class="item"><view class="iconfont down-arrow">&#xe610;</view><view>VIP连载人气</view></view><view @click="goToList(0)" class="iconfont right-arrow item">&#xe658;</view></view>
				<block v-for="(i, index) in bookList" :key="index" @click="goToChapter(i.pk, index)">
					<view>
						<view><image lazy-load="" mode="widthFix" :src="i.fields.cover_url"></image></view>
						<view class="book_name">{{ i.fields.book_name }}</view>
						<view class="chapter_name">{{ i.fields.last_chapter }}</view>
					</view>
				</block>
			</view>
			<view class="update-book-list">
				<view class="update-book-list-title" ><view class="item"><view class="iconfont down-arrow">&#xe610;</view><view>VIP新作尝鲜</view></view><view @click="goToList(1)" class="iconfont right-arrow item">&#xe658;</view></view>
				<view class="new-book">
					<view class="new-book-item"><image mode="aspectFill" src="../../static/images/douyin/4.jpg"></image></view>
					<view class="book-name">超级微信</view>
					<view class="book-description">手机balabalabalaaaasasd</view>
				</view>
				<block v-for="(i, index) in bookList" :key="index" @click="goToChapter(i.pk, index)">
					<view>
						<view><image lazy-load="" mode="widthFix" :src="i.fields.cover_url"></image></view>
						<view class="book_name">{{ i.fields.book_name }}</view>
						<view class="chapter_name">{{ i.fields.last_chapter }}</view>
					</view>
				</block>
			</view>
			<view class="book_list">
								<view class="update-book-list-title" ><view class="item"><view class="iconfont down-arrow">&#xe610;</view><view>VIP上升最快</view></view><view @click="goToList(2)" class="iconfont right-arrow item">&#xe658;</view></view>
				<view class="book_item" v-for="(i, index) in bookList" :key="index" @click="goToChapter(i.pk, index)">
					<view class="control">
						<view><image lazy-load="" mode="aspectFill" :src="i.fields.cover_url"></image></view>
						<view class="book_name">{{ i.fields.book_name }}</view>
						<!-- <view class="chapter_name">{{ i.fields.last_chapter }}</view> -->
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			bookList: []
		};
	},
	beforeCreate() {
		uni.request({
			url: 'http://api.baititong.top:8000/showBooklist/0/6', //仅为示例，并非真实接口地址。
			data: {},
			header: {},
			success: res => {
				this.bookList = res.data;
			}
		});
	},
	methods:{
		goToList(i){
			
			uni.switchTab({
				url:'../list/index'
			})
			uni.setStorage({
				key:'type',
				data:i,
			})
		}
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
		background-color: #222222;
		color: #ebcd9d;
		.control {
			display: flex;
			width: 700rpx;
			justify-content: space-between;
			.back {
				font-size: 45upx;
			}
		}
	}
}
.content {
	padding-top: 70rpx;
	background-color: #222222;
	display: flex;
	justify-content: center;
	height: 430rpx;
	align-items: center;
}
.common {
	display: flex;
	width: 750rpx;
	flex-direction: column;
	align-items: center;
	.tip {
		height: 160rpx;
		width: 750rpx;
		display: flex;
		justify-content: center;
		align-items: center;
		.tip-icon{
			width: 700rpx;
			background:linear-gradient(45deg,gold,red) ;
			height: 100rpx;
			border-radius: 50rpx;
			display: flex;
			justify-content: center;
			align-items: center;
			font-weight: bold;
		}
	}
	.book_list {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		width: 750rpx;
		.update-book-list-title{
			display: flex;
			width: 740rpx;
			padding-bottom: 20rpx;
			font-weight: bold;
			font-size: 35rpx;
			align-items: center;
			justify-content: space-between;
			.item{
				display: flex;
				align-items: center;
				.down-arrow{
					font-size: 60rpx;
					color: #ebcd9d;
				}
				
			}
			.right-arrow{
				font-size: 50rpx;
			}
			
		}
		image {
			width: 370rpx;
			height: 200rpx;
		}
		.book_name {
			padding-left: 20rpx;
			padding-top: 10rpx;
			padding-bottom: 30rpx;
			font-size: 25rpx;
		}
	}
	.update-book-list {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		
		.update-book-list-title{
			display: flex;
			align-items: center;
			padding-bottom: 20rpx;
			font-weight: bold;
			font-size: 35rpx;
			width: 740rpx;
			justify-content: space-between;
			.item{
				display: flex;
				align-items: center;
				.down-arrow{
					font-size: 60rpx;
					color: #ebcd9d;
				}
				
			}
			.right-arrow{
				font-size: 50rpx;
			}
			
		}
		.new-book{
			width: 750rpx;
			
			image{
				width: 750rpx;
			}
			.book-name{
				margin-left: 20rpx;
				font-size: 35rpx;
				font-weight: bold;
			}
			.book-description{
				margin-left: 20rpx;
				font-size: 25rpx;
				padding: 10rpx 0;
				color: #E5E5E5;
				margin-bottom: 20rpx;
			}
		}
		image {
			width: 240rpx;
		
		}
		.book_name {
			padding-left: 20rpx;
			padding-top: 10rpx;
			padding-bottom: 30rpx;
			font-size: 25rpx;
		}
	}
}
</style>
