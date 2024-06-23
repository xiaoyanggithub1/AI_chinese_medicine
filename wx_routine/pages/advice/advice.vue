<template>
	<view class='app-container'>
		<!-- 头部图片 -->
		<view class="header-container">
			<img src="https://axy-uni.oss-cn-beijing.aliyuncs.com/fankui.png" alt="">
		</view>
		<!-- 常见文件 -->
		<view class="issue-container">
			<view class="issue-header">
				<view class="title">
					<text>常见问题</text>
				</view>
				<view class="all">
					<text>全部</text>
				</view>

			</view>

			<view class="issue-item">
				<view class="item" v-for="(item,index) in issueList" :key="index" @click="clickIssue(item)">
					{{item.text}}
				</view>
			</view>
		</view>

		<!-- 我要发言 -->
		<view class="speak" @click="goFrom()">
			我要发言
		</view>
	</view>
</template>

<script>
	import {
		updateManagers
	} from '@/api/set/set.js'
	import {
		removeToken
	} from '@/utils/auth.js'
	export default {
		data() {
			return {
				issueList: [{
						id: 1,
						text: '账号与密码'
					},
					{
						id: 2,
						text: 'AI问诊聊天'
					},
					{
						id: 3,
						text: '收藏问题'
					},
					{
						id: 4,
						text: '其他问题'
					}

				],

				from: {
					username: 'jihu',
					password: ''

				}

			}
		},
		methods: {
			// 点击issue
			clickIssue(item) {
				console.log(item, 123)
				uni.navigateTo({
					url: '/pages/advice/advice_item/advice_item?id='+item.id
				});
			},

			goFrom() {
				uni.navigateTo({

					url: '/pages/advice/from',
					// animationType: 'pop-in',
					animationDuration: 200
				});
			}

		}
	}
</script>

<style lang="scss" scoped>
	.app-container {
		width: 100%;

		.header-container {
			padding: 20rpx;
			width: calc(100% - 40rpx);
			height: 350rpx;

			// background-color: red;
			img {
				width: 100%;
				height: 350rpx;
			}

		}

		.issue-container {
			margin-top: 20rpx;
			padding: 20rpx;
			width: calc(100% - 40rpx);

			.issue-header {
				width: 100%;
				display: flex;
				justify-content: space-between;
				align-items: center;
				margin-bottom: 20rpx;

				.title {
					font-weight: 600;
					font-size: 32rpx;
				}

				.all {
					font-size: 24rpx;
				}
			}

			.issue-item {
				width: 100%;

				.item {
					height: 70rpx;
				}
			}
		}

		.speak {
			width: 250rpx;
			position: fixed;
			height: 80rpx;
			line-height: 80rpx;
			bottom: 50rpx;
			left: calc(50% - 125rpx);
			background-color: #006BFC;
			color: #fff;
			text-align: center;
			border-radius: 100rpx;

		}

	}
</style>