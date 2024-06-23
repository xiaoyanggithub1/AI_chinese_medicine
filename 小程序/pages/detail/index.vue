<template>
	<view class="content">
		<image class="image_view" src="https://axy-uni.oss-cn-beijing.aliyuncs.com/1ABAFAAFDEDEF426F65BAC069C2D6370.jpg">
		</image>
		<view v-if="isAdd == 2">
			<view class="picture">
				<view>

					<image :src='baseURL + "/" + herbal_data.picture_path'></image>
				</view>
			</view>
			<view class="text">
				<view class="name,herbal">
					<view>
						{{ herbal_data.name }}
					</view>
					<view>
						<image class="icon" src="../../static/ceIcon.png"></image>
						<text class="cText" @click="favClick()" style="font-size: 30rpx;"> 收藏</text>
					</view>
				</view>
				<view class="all_detail">
					<view class="all_detail_text">
						{{ herbal_data.name + '，中药名。功效有' + herbal_data.effect + "药性" + herbal_data.property }}
					</view>
					<view class="all_detail_ul">
						<view class="li">
							<view class="li_name">
								中文名
							</view>
							<view class="li_answer">
								{{ herbal_data.name }}
							</view>
						</view>
						<view class="li">
							<view class="li_name">
								别名
							</view>
							<view class="li_answer">
								{{ herbal_data.surname }}
							</view>
						</view>
					</view>
				</view>
			</view>
			<view class="interval">
			</view>
			<view class="text">
				<view class="names">
					药材功效
				</view>
				<view class="all_detail">
					<view class="all_detail_text">
						{{ herbal_data.effect }}
					</view>
				</view>
			</view>
			<view class="interval">
			</view>
			<view class="text">
				<view class="names">
					药性
				</view>
				<view class="all_detail">
					<view class="all_detail_text">
						{{ herbal_data.property }}
					</view>
				</view>
			</view>
			<view class="interval">
			</view>
			<view class="text">
				<view class="names">
					注意事项
				</view>
				<view class="all_detail">
					<view class="all_detail_text">
						{{ herbal_data.manage }}
					</view>
				</view>
			</view>
		</view>

		<view v-else>
			<view class="text">
				<view class="name,detail">
					<view class="">
						{{ prescription_data.name }}
					</view>
					<view>
						<text @click="favClick()" style="font-size: 30rpx;"> 收藏</text>

						<!-- <uni-fav :checked="checkList" class="favBtn" @click="favClick()" circle /> -->

					</view>
				</view>
				<view class="all_detail">
					<!-- 					<view class="all_detail_text">
						{{prescription_data.name+prescription_data.manage}}
					</view> -->
					<view class="all_detail_ul">
						<view class="li">
							<view class="li_name">
								出处
							</view>
							<view class="li_answer">
								{{ prescription_data.provenance }}
							</view>
						</view>
						<view class="li">
							<view class="li_name">
								功效
							</view>
							<view class="li_answer">
								{{ prescription_data.effect }}
							</view>
						</view>

						<view class="li">
							<view class="li_name">
								治疗症状
							</view>
							<view class="li_answer">
								{{ prescription_data.major }}
							</view>
						</view>
					</view>
				</view>
			</view>
			<view class="interval">
			</view>
			<view class="text">
				<view class="names">
					治疗疾病以及注意事项
				</view>
				<view class="all_detail">
					<view class="all_detail_text">
						{{ prescription_data.name + prescription_data.manage }}
					</view>
				</view>
			</view>
			<view class="text">
				<view class="names">
					用法用量
				</view>
				<view class="all_detail">
					<view class="all_detail_text">
						{{ prescription_data.compose }}
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
import { managerSc } from '@/api/about/index.js'
import { baseURL, imgURL } from "@/config/index.js"
import {
	cxzhongyao,
	cxfangji
} from "../../api/intelligent.js"
export default {
	data() {
		return {
			isAdd: '',
			herbal_data: [],
			prescription_data: [],
			checkList: false,

		}
	},

	computed: {
		baseURL() {
			return baseURL
		}
	},

	onLoad: function (option) {
		this.isAdd = option.value
		if (this.isAdd == 1) {
			this.prescription_data = JSON.parse(decodeURIComponent(option.data))
		} else {
			this.herbal_data = JSON.parse(decodeURIComponent(option.data))
		}
	},

	methods: {
		favClick(index) {
			const id = this.prescription_data.id || this.herbal_data.id
			managerSc({ sc: id }).then(res => {
				if (res.code == 0) {
					uni.$u.toast('收藏成功')
				}
			})
			// console.log(this.prescription_data,this.herbal_data)
			// this.checkList = !this.checkList
			// console.log(this.checkList);
			// this.$forceUpdate()
			// let userInfo = uni.getStorageSync('userInfo')
			// if (userInfo != '') {
			// 	uni.navigateTo({
			// 		// url: "/pages/Application/index"
			// 	})
			// } else {
			// 	uni.navigateTo({
			// 		url: "../login/index"
			// 	})
			// }
		}

	}
}
</script>

<style lang="scss" scoped>
.content {
	width: 100%;
	height: 100vh;
	overflow-y: auto;

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

	.picture {
		aspect-ratio: 16/9;
		width: 100%;

		image {
			aspect-ratio: 16/9;
			width: 100%;
			display: block;
		}
	}

	.text {
		padding: 16px;

		.icon {
			width: 45rpx;
			height: 45rpx;
		}

		.name {
			font-size: 28px;
			padding-bottom: 16px;
			border-bottom: 1px solid #e6e6e6;
		}

		.herbal {
			display: flex;
			justify-content: space-between;

			view:first-child {
				// background-color: darkblue;
			}

			:last-child {
				display: flex;
				align-items: center;
			}
		}

		.detail {
			display: flex;
			justify-content: space-between;

			view:first-child {
				// background-color: darkblue;
			}

			:last-child {
				display: flex;
				align-items: center;
			}
		}

		.names {
			font-size: 23px;
			padding-bottom: 16px;
			padding-top: 16px;
		}

		.all_detail {
			margin-top: 16px;

			.all_detail_text {
				width: 100%;
				word-wrap: break-word;
			}

			.all_detail_ul {
				margin-top: 32px;
				width: 100%;

				.li {
					// width: 100%;
					display: flex;
					padding-bottom: 5px;

					.li_name {
						width: 25%;
						margin-right: 10%;
						word-wrap: break-word;
					}

					.li_answer {
						width: 75%;
						word-wrap: break-word;
					}
				}
			}
		}
	}

	.interval {
		width: 100%;
		height: .08rem;
		background-color: #f5f5f5;
	}
}
</style>