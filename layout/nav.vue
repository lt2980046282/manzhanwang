<template>
	<view>
		<view class="nav_list">
			<view v-for="(i, index) in nav" :key="index"  :style="{ color: index == navIndex ? '#ff0000' : 'black' }" class="nav_item">
				<navigator animation-type="pop-in" animation-duration="300" :url="i.url">
					<view class="control">
						<view class="iconfont">{{ i.icon }}</view>
						<view style="margin-left: -2rpx;">{{ i.name }}</view>
					</view>
				</navigator>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			nav: [
				{ name: '首页', icon: '\ue686', url: '/pages/index/index' },
				{ name: '分类', icon: '\ue659', url: '/pages/list/index' },
				{ name: '书架', icon: '\ue602', url: '/pages/bookshelf/index' },
				{ name: '我的', icon: '\ue64c', url: '/pages/my/index' }
			],
		};
	},
	methods:{

	},
	props:{
		navIndex:{
			type:Number,
			default:0,
		}
	}
};
</script>

<style>
.nav_list {
	display: flex;
	justify-content: center;
	align-items: center;
	position: fixed;
	bottom: 0;
	left: 0;
	width: 750rpx;
	background: #ffffff;
	height: 120rpx;
	font-size: 20rpx;
}
.nav_item {
	width: 187.5rpx;
	display: flex;
	justify-content: center;
	align-items: center;
	height: 120rpx;
}
.control {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-content: center;
	text-align: center;
}
</style>
