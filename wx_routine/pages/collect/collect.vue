<template>
	<view class="app-container">
		<view class="container" v-for="(item,index) in scList" :key="index" @click="toDetils(item)">
			<view class="item-img">
				<img :src="item.img" alt="">
			</view>
			<view class="item-container">
				<view class="item-title">
					<text>{{item.title}}</text>
				</view>
				<view class="item-content">
					{{item.content}}
				</view>
			</view>

		</view>
	</view>
</template>

<script>
	import {
		managerScs
	} from '@/api/collect/index.js'
	export default {
		data() {
			return {
				scList: [{
					id: 1,
					img: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/1612743177396_2.jpeg',
					title: "人参",
					content: '人参适用于调整血压、恢复心脏功能、神经衰弱级身体虚弱等症'

				}, {
					id: 2,
					img: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/808a782848f71d20.jpg',
					title: "决明子",
					content: '决明子可起到解表清热、清肝明目、润肠通便的作用。'

				}, {
					id: 3,
					img: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/QJ9125721809.jpg',
					title: "当归",
					content: '当归是中医中最常用的药，多用于煲汤，特别对贫血患者是最好的。'

				},
				{
					id: 4,
					img: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/u%3D338119390%2C3655726422%26fm%3D253%26fmt%3Dauto%26app%3D138%26f%3DJPEG.webp',
					title: "半夏",
					content: '半夏辛散温燥有毒，主入脾胃，兼入肺。具有镇咳祛痰、降逆止呕、抗溃疡、增强肝功能等功效。'
				
				}]
			}
		},
		onLoad() {
			this.init()

		},
		methods: {
			init() {
				// 这里至少要给一个name
				// managerScs().then(res => {
				// 	this.scList = res.data
				// })

			},
			toDetils(item) {
				uni.navigateTo({
					url: "/pages/detail/index"
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	.app-container {
		width: 100%;
		min-height: 100vh;
		background-color: #f9f9f9;
		

		.container {
			padding: 20rpx;
			width: calc(100% - 40rpx);
			margin-bottom: 40rpx;
			display: flex;
			justify-content: space-between;
			background-color: #fff;
          border-bottom: 5px solid #c6955d;

			.item-img {
				width: 300rpx;
				height: 200rpx;
				overflow: hidden;
				border-radius: 20rpx;
				margin: 10px;

				img {
					width: 100%;
					height: 100%;
					
				}
			}

			.item-container {
				width: calc(100% - 300rpx);
				
				.item-title {
					margin: 10px;
					font-size: 50rpx;
					color: #c6955d;
				}
			}
		}
	}
</style>