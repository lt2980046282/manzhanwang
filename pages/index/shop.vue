<template>
	<view>
		<view class="nav">
			<view class="container">
				<navigator open-type="navigateBack">
					<view class="iconfont back">&#xe606;</view>
				</navigator>
				<view class="title">积分商城</view>
				<view></view>
			</view>
		</view>
		<view class="common">
			<view class="container">
				<view class="info">
					<view class="info-item">
						<view>积分</view>
						<view>1370</view>
					</view>
					<view class="info-item">
						<view>兑换记录</view>
					</view>
				</view>
				<view class="banner"></view>
				<view class="title">- 积分兑换商品 -</view>
				<view class="goods">
					<view  v-for="i in 10" :key="i" class="good-item">
						<image class="good-cover" src="../../static/BasicsBg.png"></image>
						<view class="good-title">漫客栈1天黑金VIP</view>
						<view class="good-credit">
							<view class="good-num">1250</view>积分
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
</script>

<style lang="scss">
	.nav {
		height: 100rpx;
		width: 750rpx;
		position: fixed;
		background: #FFFFFF;
		display: flex;
		justify-content: center;
		align-items: center;
		border-bottom: 2rpx solid #E5E5E5;
		z-index: 100;
		.container {
			width: 700rpx;
			display: flex;
			justify-content: space-between;
			align-content: center;

		}
	}

	.common {
		padding-top: 100rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 750rpx;
		
		.container {
			width: 700rpx;
			display: flex;
			flex-direction: column;
			align-items: center;
			.info {
				display: flex;
				padding: 20rpx 0 ;
				font-size: 28rpx;
				.info-item {
					width: 350rpx;
					display: flex;
				}
			}

			.banner {
				background: linear-gradient(45deg, purple, red);
				width: 700rpx;
				height: 100rpx;
				border-radius: 50rpx;
			}
			.title{
				padding: 20rpx 0;
				color: #c0c0c0;
				font-size: 24rpx;
			}
			.goods{
				display: flex;
				flex-wrap: wrap;
				justify-content: space-between;
				.good-item{
					
					.good-cover{
						width: 330rpx;
						height: 220rpx;
						border-radius: 10rpx;
						padding: 10rpx 0;
					}
					.good-title{
						font-size: 28rpx;
						font-weight: bold;
						
					}
					.good-credit{
						display: flex;
						padding: 10rpx 0;
						font-size: 24rpx;
						.good-num{
							color: #FF8C00;
							padding-right: 3rpx;
							
						}
					}
					
				}
			}
		}
	}
</style>
