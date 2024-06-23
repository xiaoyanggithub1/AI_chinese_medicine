<template>
	<view class="content">
		<view class="head_box">
			<view class="head_box">
				<view class="head_text">
					<view><text class="title">AI中医馆</text></view>

					<text class="sub_title">专属您的私人医生</text>
				</view>
				<view class="head_image">
					<!-- <image src="../../static/ys2.png" class="doc_image"></image> -->
					<image src="https://axy-uni.oss-cn-beijing.aliyuncs.com/homeDoctor.png" class="doc_image"></image>
				</view>
				<view class="query_box">
					<view class="menu">
						<!-- 第一个参数是每一项item 第二个参数是索引 index -->
						<view v-for="(item,index ) in menus" :key="index">
							<view class="item">
								<view class="image_view" :style="{background:item.bg}" @click="clickTab(item)">
									<image :src="item.icon" class="image"></image>
								</view>
								<text class="text">{{item.txt}}</text>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>

		<!-- jiezhe -->
		<view class="new-container">
			<view class="new-title">
				新闻资讯
			</view>
			<view class="new-item" v-for="(item,index) in newLish" :key='index' @click="toNew(item)">
				<view class="item-container">
					<view class="item-img" style="padding: 0;">
						<img :src="item.img" alt="">
					</view>
					<view class="item-title">
						{{item.title}}
					</view>
				</view>

				<view class="item-info">
					<view class="time">
						时间：{{item.time}}
					</view>
					<view class="other">
						阅读 {{item.see}}
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
				menus: [{
						id: 1,
						bg: 'linear-gradient(0deg,rgba(209, 155, 105),rgba(209, 155, 105))',
						icon: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/chaoxun3.png',
						txt: '中药查询',
					},
					{
						id: 2,
						bg: 'linear-gradient(0deg,rgba(209, 155, 105),rgba(209, 155, 105))',
						icon: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/tiweng5.png',
						txt: 'AI智能问诊',

					},
					{
						id: 3,
						bg: 'linear-gradient(0deg,rgba(209, 155, 105),rgba(209, 155, 105))',
						icon: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/111.png',
						txt: '方剂查询',
					}
				],

				newLish: [{
					id: 1,
					title: '安徽亳州谯城区风华桐乡路小学开展“中医药文化进校园”活动',
					time: '2023-05-04',
					see: '500',
					img: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/pic1%20anhui.jpg.crdownload'
				}, {
					id: 2,
					title: '吉林省首届“阅读中华悦动青春”大学生读书节开幕',
					time: '2023-05-04',
					see: '450',
					img: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/pic2%20jilin.jpg.crdownload'
				}, {
					id: 3,
					title: '湖南郴州市北湖实验学校学生在制作中药香囊',
					time: '2023-05-04',
					see: '600',
					img: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/pic3%20hunan.jpg.crdownload'
				}, {
					id: 4,
					title: '湖北省中医养生功法大赛决赛在武汉江滩举行',
					time: '2023-05-04',
					see: '420',
					img: 'https://axy-uni.oss-cn-beijing.aliyuncs.com/pic4%20hubei.jpg.crdownload'
				}]
			}
		},
		onLoad() {

		},
		methods: {
			clickTab(item) {
				if (item.id == 3) {
					//方剂为1
					uni.navigateTo({
						url: '../CM_inquire/index?value=1'
					});
				} else if (item.id == 2) {
					uni.switchTab({
						url: '/pages/chat/chat'
					});
				} else if (item.id == 1) {
					// 中药为2
					uni.navigateTo({
						url: '../CM_inquire/index?value=2'
					});
				}
			},

			toNew(item) {
				console.log(item.id)
				uni.navigateTo({
					url: '/pages/home/new?id='+item.id
				});
			}
		}
	}
</script>

<style lang="scss" scoped>
	.content {
		width: 100%;
		height: 1500rpx;
		background-color: #ebebeb;

		.head_box {
			position: relative;
			width: 100%;
			height: 500rpx;
			background-color: #c6955d;
			margin-bottom: 80px;

			.head_text {
				padding: 50rpx;
				margin-left: 15rpx;

				.title {
					font-size: 60rpx;
					font-weight: bold;
					color: white;
				}

				.sub_title {
					font-size: 30rpx;
					color: white;
				}
			}

			.head_image {
				position: absolute;
				
				top: 35rpx;
				margin-left: 500rpx;


				.doc_image {
					position: absolute;
					top: -10rpx;
					right: -117rpx;
					width: 272rpx;
					height: 344rpx;
				}
			}

			.query_box {
				position: absolute;
				top: 350rpx;
				left: 50%;
				transform: translate(-50%);
				width: 660rpx;
				height: 250rpx;
				background-color: white;
				border-radius: 20px;
				box-shadow: 0px 10px 10px 0px rgba(0, 161, 124, 0.1);

				.menu {
					margin-left: 35rpx;
					margin-right: 35rpx;

					padding-left: 5rpx;
					padding-right: 5rpx;
					padding-bottom: 38rpx;
					height: realSize(370rpx);
					border-radius: 10px;
					display: flex;
					flex-direction: row;
					align-items: stretch;
					justify-content: space-between;

					.item {
						display: flex;
						margin-top: 55rpx;
						flex-direction: column;
						align-items: center;
						justify-content: center;

						.image_view {
							width: 60px;
							height: 60px;
							border-radius: 30px;
							display: flex;
							align-items: center;
							justify-content: center;

							.image {
								width: 30px;
								height: 30px;
							}
						}

						.txt {
							margin-top: 5px;
							font-size: 14px;
							color: rgba(51, 51, 51, 1);
						}
					}
				}
			}
		}

		.new-container {
			background-color: #fff;
			margin-top: 150rpx;

			view {
				padding: 20rpx;
				width: calc(100% - 40rpx);
			}

			.new-title {
				font-size: 40rpx;
				font-weight: 600;
				color: #c6955d;
			}

			.new-item {
				// padding: 0;


				.item-container {
					display: flex;
					justify-content: flex-start;
					padding: 0;

					img {
						width: 300rpx;
						height: 170rpx;
					}

					.item-title {
						padding: 0;

						font-size: 30rpx;
						font-weight: 600;
						color: #000;
						overflow: hidden;
						display: -webkit-box;
						-webkit-box-orient: vertical;
						-webkit-line-clamp: 3;
					}
				}

				.item-info {
					padding: 0;
					width: 100%;
					font-size: 30rpx;
					color: #999aaa;
					display: flex;
					justify-content: space-between;

					.time {
						padding: 0;
					}

					.other {
						padding: 0;
						text-align: right;
					}

				}


			}
		}
	}
</style>