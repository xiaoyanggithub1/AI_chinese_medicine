<template>
	<view class="page">
		<view class="top">
			<view class="background"></view>
		</view>
		<view class="user-card">
			<view class="card">
				<view class="top">
					<view class="userImage">
						<open-data type="userAvatarUrl"></open-data>
					</view>
				</view>
				<view class="bottom">
					<view class="left">
						<view class="user-text">
							<open-data type="userNickName"></open-data>
						</view>
						<view class="user-phone"> 171****4133 </view>
					</view>
					<view class="right flex-center" style="position: absolute;">
						<image class="myself" style="position: relative;left: 250px;"
							src="@/static/image/other/right_arrow.png" mode="aspectFit" @click="btn_setting()"></image>
					</view>
				</view>
			</view>
		</view>
		<view class="list-card">
			<view class="card">
				<!-- <view class="item item-bottom-solid">
         <view class="left flex-center">
            <image src="@/static/image/other/myqiu.png" mode="aspectFit"></image>
          </view>
         <view class="center">
            <text>参加的活动</text>
          </view>
         <view class="right flex-center">
           <image src="@/static/image/other/right_arrow.png" mode="aspectFit" @click="btn()"></image>
          </view>
        </view> -->
			</view>
			<view class="card">
				<view class="item item-bottom-solid">
					<view class="left flex-center">
						<image src="@/static/image/other/my1.png" mode="aspectFit"></image>
					</view>
					<view class="center">
						<text>帮助与反馈</text>
					</view>
					<view class="right flex-center">
						<image class="myself" src="@/static/image/other/right_arrow.png" mode="aspectFit"
							@click="btn_advice()"></image>
					</view>
				</view>
			</view>
			<view class="card">
				<view class="item item-bottom-solid">
					<view class="left flex-center">
						<image src="@/static/image/other/my2.png" mode="aspectFit"></image>
					</view>
					<view class="center">
						<text>我的收藏</text>
					</view>
					<view class="right flex-center">
						<image class="myself" src="@/static/image/other/right_arrow.png" mode="aspectFit"
							@click="btn_collect()"></image>
					</view>
				</view>
			</view>
		</view>
		<view class="quit flex-center">
			<view class="btn flex-center" @click="btn_out()">
				退出登录
			</view>
		</view>
	</view>
</template>
<script>
	//import {  } from "@/common/api/{$}.js";
	export default {
		data() {
			return {};
		},
		onLoad() {
			console.log('init')
			uni.setStorage({
				key: 'axy',
				data: '123',

			});

		},
		onShow() {
			console.log('show')
		},
		methods: {
			btn_setting() {
				uni.navigateTo({

					url: '/pages/setting/setting',
					// animationType: 'pop-in',
					animationDuration: 200
				});
			},
			btn_collect() {
				// 这里
				/* uni.$u.toast('功能开发中')
				return
				 */
				uni.navigateTo({

					
					
					url: '/pages/collect/collect',
					// animationType: 'pop-in',
					animationDuration: 200
				});
			},
			btn_advice() {
				uni.navigateTo({

					url: '/pages/advice/advice',
					// animationType: 'pop-in',
					animationDuration: 200
				});
			},
			// 驼峰命名
			btn_out() {
				this.$store.dispatch("Logout").then(() => {
					//判断有没有退出成功
					uni.$u.toast('退出成功')

					setTimeout(() => {
						uni.reLaunch({
							url: '/pages/login/index'
						})
					}, 500)

				})
			},

		},

		//监听页面初始化，其参数同 onLoad 参数，为上个页面传递的数据，参数类型为 Object（用于页面传参），触发时机早于 onLoad
		onInit() {},
		//监听页面加载，其参数为上个页面传递的数据，参数类型为 Object（用于页面传参）
		onLoad() {},
		//监听页面初次渲染完成。注意如果渲染速度快，会在页面进入动画完成前触发
		onReady() {},
		//监听页面显示。页面每次出现在屏幕上都触发，包括从下级页面点返回露出当前页面
		beforeDestroy() {},
		//页面滚动到底部的事件（不是scroll-view滚到底），常用于下拉下一页数据。
		onReachBottom() {},
		onShareAppMessage(res) {},
		created() {},

	};
</script>

<style lang="scss" scoped>
	.top {
		height: 250rpx;
		position: relative;

		.background {
			background-color: #c6955d;
			border-bottom-left-radius: 22px;
			border-bottom-right-radius: 22px;
			position: absolute;
			height: 180rpx;
			width: 100%;
		}
	}

	.icon {
		color: #96a1ae;
		font-size: 40rpx;
	}

	.myself {
		margin-left: $uni-border-color;
		width: 50px;
		height: 50px;
	}

	.user-card {
		height: 170rpx;
		padding: 0 15px;

		.card {
			position: relative;
			bottom: 62px;
			height: 250rpx;
			background-color: white;
			border-radius: 5px;

			.top {
				height: 30%;
				position: relative;

				.userImage {
					position: absolute;
					bottom: 24%;
					left: 10%;
					width: 150rpx;
					height: 150rpx;
					overflow: hidden;
					border-radius: 50%;
					border: 2px solid white;
				}
			}

			.bottom {
				display: flex;
				height: 70%;

				.left {
					width: 80%;
					height: 100%;
					position: relative;

					.user-text {
						width: 100%;
						font-size: 1.6em;
						padding-left: 80rpx;
						height: 50%;
					}

					.user-phone {
						color: #96a1ae;
						padding-left: 80rpx;
						height: 50%;
						width: 100%;
						font-size: 0.9em;
					}
				}

				.right {
					width: 20%;
					height: 50%;
				}
			}
		}
	}

	.list-card {
		padding: 0 15px;

		.card {
			border-radius: 5px;
			position: relative;
			background-color: white;
			border-radius: 5px;
			padding: 5px 30px;

			.item {
				display: flex;
				height: 120rpx;

				.left {
					width: 10%;

					image {
						width: 70rpx;
						height: 70rpx;
					}
				}

				.center {
					width: 65%;
					display: flex;
					justify-content: start;
					align-items: center;
					font-size: 1.1em;
				}

				.right {
					width: 20%;
					justify-content: flex-end;
				}
			}
		}
	}

	.item-bottom-solid {
		border-bottom: 1px solid #d4d6da;
	}

	.quit {
		height: 100rpx;
		margin-top: 50px;

		.btn {
			background-color: #c6955d;
			border-radius: 30px;
			width: 80%;
			color: white;
			font-size: 1.2em;
			height: 100%;
		}
	}

	.flex-center {
		display: flex;
		justify-content: center;
		align-items: center;
	}
</style>