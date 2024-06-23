<template>
	<view class="ad_box">
		<view class="image_box">
			
			<view class="item" v-for="(item,index) in adviceList" :key="index"><text v-if="id==item.id">{{item.text}}</text></view>
			<image class="image_view" src="https://axy-uni.oss-cn-beijing.aliyuncs.com/1ABAFAAFDEDEF426F65BAC069C2D6370.jpg"></image>
		</view>
			
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				id:1,
				adviceList:[{
					id: 1,
						text: '如果你忘记了用户名或者密码,你可以点击头像旁边的箭头去修改哦!',
					},
					{
						id: 2,
						text: '你可以把你的症状告诉机器人，它会给你提供其他可能的出现的症状。尽量描述详细一点哦！'
					},
					{
						id: 3,
						text: '你可以收藏自己认为有用的中药、方剂等，下次需要使用时可以直接浏览，方便快捷!'
					},
					{
						id: 4,
						text: '你可以提出一些其他问题，我们会尽量完善，谢谢你宝贵的意见！'
				}]
			}
		},
		methods: {
			
		},
		onLoad(options){
			this.id=options.id
		}
	}
</script>

<style lang="scss">
	
	.image_box {
		width: 100%;
		height:1450rpx;
		position: relative;
		z-index: 0; 
		
		.item{
			
			
			width: 50%;
			height: 50%;
			align-items: center;
			position: absolute;
			font-size: 37px;
			color: white;
			left: 53rpx;
			top: 353rpx;
		}
		}
	
	.image_view {
		width: 100%;
		height: 5000rpx;
	    position: absolute;
	    z-index: -1;
	    left: 0;
	    right: 0;
	    bottom: 0;
	    right: 0;
	    width: 100%;
	    height: 100%;
	}
	
</style>
