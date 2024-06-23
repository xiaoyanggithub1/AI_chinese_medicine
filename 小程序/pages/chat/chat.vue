<template>
	<view>

		<view class="box-1" id="list-box" ref="overf">
			<view class="talk-list">
				<view v-for="(item,index) in talkList" :key="index" :id="`msg-${item.id}`">

					<view class="item flex_col" :class=" item.type == 1 ? 'push':'pull' ">
						<image :src="item.pic" mode="aspectFill" class="pic"></image>
						<view class="content">
							<!-- 基本文本回复 -->
							<view class="text">
								<text>{{item.content.text}}</text>
							</view>

							<!-- 你可能还想问 -->
							<view class="hava-possible-issues"
								v-if="item.content.havePossibleIssues&&item.content.havePossibleIssues.length>0">
								<!-- 分割线 -->
								<view class="divider">
								</view>

								<view class="title">
									<!-- 你可能还想问： -->
									{{maybe_question}}
								</view>

								<view class="issues-container">
									<view class="issues-item" v-for="(itm,idx) in item.content.havePossibleIssues"
										:key="idx" @click="clickIssues(itm,item)">
										<text :class="{textType:item.types==2}">{{itm.text}}</text>
									</view>
								</view>
							</view>

							<!-- 可能存在的症状 -->
							<view class="hava-possible-issues"
								v-if="item.content.haveSymptom&&item.content.haveSymptom.length>0">
								<!-- 分割线 -->
								<view class="divider">
								</view>

								<view class="title">
									你是否存在以下情况：
								</view>

								<view class="issues-container">
									<view class="symptom-item" v-for="(itm,idx) in item.content.haveSymptom" :key="idx"
										@click="clickSymptom(itm,item)">
										<text :class="{textType:item.types==2}">{{itm.text}}</text>
									</view>
								</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		<view class="box-2" ref="box2">
			<view class="flex_col">
				<view class="flex_grow">
					<input type="text" class="content" v-model="content" placeholder="请输入问题"
						placeholder-style="color:#DDD;" :cursor-spacing="6">
				</view>
				<button class="send" @tap="send">发送</button>
			</view>
		</view>
	</view>
</template>

<script>
	import {
		query
	} from "../../api/intelligent.js"
	import search from "../../uni_modules/uview-ui/libs/config/props/search.js";

	export default {
		data() {
			return {
				maybe_question: "你可能还想问：",
				talkList: [], //消息列表
				ajax: {
					rows: 20, //每页数量
					page: 1, //页码
					flag: true, // 请求开关
					loading: true, // 加载中
					loadText: '正在获取消息'
				},
				content: '',
				dom: null,
				pathogen: ""
			}
		},
		mounted() {
			// ok
			if (uni.getSystemInfoSync().uniPlatform != "mp-weixin") {
				this.$refs.box2.$el.style.bottom = '50px'

				

			}

		},
		onPageScroll(e) {

		},
		onLoad() {



		},
		omShow() {},

		created() {
			let data = {
				id: new Date().getTime(),
				content: {
					text: `欢迎来到AI中医馆,你可以向我们询问,例如:\n1.百日咳可以用什么方剂治疗\n2.我咳嗽怎么办\n3.焦虑症吃点什么好\n4.得了百日咳不能吃什么\n5.南瓜子仁可以治疗什么疾病\n`,
				},
				type: 0,
				pic: "https://axy-uni.oss-cn-beijing.aliyuncs.com/pic.png"
			}
			this.talkList.push(data);
		},

		methods: {
			// 发送信息
			send() {
				if (!this.content) {
					uni.showToast({
						title: '请输入有效的内容',
						icon: 'none'
					})
					return;
				}

				// uni.hideLoading();
				// 将当前发送信息 添加到消息列表。
				let data = {
					"id": new Date().getTime(),
					content: {
						text: this.content,
					},

					"type": 1,
					"pic": "https://axy-uni.oss-cn-beijing.aliyuncs.com/user.png"
				}
				this.talkList.push(data);

				let pathogen = {
					search: data.content.text
				}
				this.pathogen = pathogen

				this.$nextTick(() => {
					let search_data = {
						search: this.pathogen.search
					}
					//问题请求
					query(search_data).then((res) => {

						const res_type = res.type
						const res_variety = res.variety
						const res_orig = res.orig
						// console.log(res_type,'res_type')
						if (res_type == 0) {
							let data = {
								id: new Date().getTime(),
								content: {
									text: res.data,
								},
								type: 0,
								pic: "/static/image/other/pic.png"
							}
							this.talkList.push(data);
						} else if (res_type == 1) {
							let maybe_inquire = []
							if (res_variety == 1) {
								// console.log("ssss");
								let a = [{
									text: '你可能还想问' + res_orig + '的用法？'
								}, {
									text: '你可能还想问' + res_orig + '可以治疗的疾病？'
								}, {
									text: '你可能还想问' + res_orig + '由什么中药组成？'
								}]
								maybe_inquire = a
							} else if (res_variety == 2) {
								let a = [{
									text: '你可能还想问' + res_orig + '的用法？'
								}, {
									text: '你可能还想问' + res_orig + '可以治疗的疾病？'
								}, {
									text: '你可能还想问' + res_orig + '由什么中药组成？'
								}]
								maybe_inquire = a
							} else if (res_variety == 3) {
								let a = [{
									text: '1.你可能还想问' + res_orig + '可以治疗的疾病？'
								}, {
									text: '2.你可能还想问' + res_orig + '由什么中药组成？'
								}]
								maybe_inquire = a
							} else if (res_variety == 4) {
								let a = [{
									text: '1.你可能还想问' + res_orig + '的用法？'
								}, {
									text: '2.你可能还想问' + res_orig + '可以治疗的症状？'
								}, {
									text: '3.你可能还想问' + res_orig + '由什么中药组成？'
								}]
								maybe_inquire = a
							} else if (res_variety == 5) {
								let a = [{
									text: '1.你可能还想问' + res_orig + '的用法？'
								}, {
									text: '2.你可能还想问' + res_orig + '可以治疗的疾病？'
								}, {
									text: '3.你可能还想问' + res_orig + '由什么中药组成？'
								}]
								maybe_inquire = a
							} else if (res_variety == 6) {
								let a = [{
									text: '1.你可能还想问' + res_orig + '可以治疗的疾病？'
								}, {
									text: '2.你可能还想问' + res_orig + '的用法？'
								}, {
									text: '3.你可能还想问' + res_orig + '可以治疗的症状？'
								}]
								maybe_inquire = a
							} else if (res_variety == 7) {
								let a = [{
									text: '1.你可能还想问' + res_orig + '可以治疗的疾病？'
								}, {
									text: '2.你可能还想问' + res_orig + '的用法？'
								}, {
									text: '3.你可能还想问' + res_orig + '可以治疗的症状？'
								}]
								maybe_inquire = a
							} else if (res_variety == 8) {
								let a = [{
									text: res_orig + '可以吃的食物'
								}]
								maybe_inquire = a
							} else if (res_variety == 9) {
								let a = [{
									text: res_orig + '不可以吃的食物'
								}]
								maybe_inquire = a
							} else if (res_variety == 10) {
								let a = [{
									text: '这些疾病' + '可以用什么方剂治疗'
								}, {
									text: '这些疾病' + '吃点什么好'
								}]
								maybe_inquire = a
							} else if (res_variety == 11) {
								let a = [{
									text: '这些疾病' + '可以用什么方剂治疗'
								}, {
									text: '这些疾病' + '吃点什么好'
								}]
								maybe_inquire = a
							} else if (res_variety == 12) {
								let a = [{
									text: '为你查找到了以下疾病或症状，你想查找那种疾病或症状呢？'
								}]
								maybe_inquire = a
							}
							let data = {
								id: new Date().getTime(),
								content: {
									text: res.data,
									havePossibleIssues: maybe_inquire,
								},
								type: 0,
								types: res_type,
								pic: "/static/image/other/pic.png"
							}
							this.talkList.push(data);

						} else if (res_type == 2) {

							let inquire = []

							let a = 1
							for (var i in res.data) {
								var i;
								var dataObj = res.data[i];
								var obj = {
									medicine: i,
									text: a + '.' + dataObj
								};
								inquire.push(obj)
								a++
							}

							let data = {
								id: new Date().getTime(),
								content: {
									haveSymptom: inquire
								},
								type: 0,
								pic: "/static/image/other/pic.png",
								variety: res_variety,
								types: res_type,
							}
							this.talkList.push(data);
							console.log(this.talkList)
						}
						this.$nextTick(() => {
							setTimeout(() => {
								uni.pageScrollTo({
									scrollTop: 9999, // 设置一个超大值，以保证滚动条滚动到底部
									duration: 0,
								});
							}, 1000)
						})

					})
					// 清空内容框中的内容
					this.content = '';

					uni.pageScrollTo({
						scrollTop: 999999999, // 设置一个超大值，以保证滚动条滚动到底部
						duration: 0,
						success: () => {}
					});
				});
			},
			// 点击可能存在的问题
			clickIssues(item) {

				let data = item.text

				// 开始裁剪的位置
				const star = data.indexOf('你可能还想问') + 6
				data = data.substring(star, data.length)

				let search_data = {
					search: data
				}
				//问题请求
				query(search_data).then((res) => {
					let data = {
						id: new Date().getTime(),
						content: {
							text: res.data,
						},
						type: 0,
						pic: "/static/image/other/pic.png"
					}
					this.talkList.push(data);
					this.$nextTick(() => {
						setTimeout(() => {
							uni.pageScrollTo({
								scrollTop: 9999, // 设置一个超大值，以保证滚动条滚动到底部
								duration: 0,
							});
						}, 1000)
					})
				})
			},

			// 点击可能存在的症状
			clickSymptom(item, items) {
				console.log(item, items);
				let text = item.text.split('.').slice(-1)


				if (items.variety == 5) {
					const search = item.medicine + '用法'
					this.content = search
					this.send()
					// query({search:item.medicine+'方剂组成'}).then(res=>{
					// 	console.log(res,'res')
					// })
				}
				let data = {
					id: new Date().getTime(),
					content: {
						text: text[0] + "。这些症状适应的方剂是：" + item.medicine,
					},
					type: 0,
					pic: "/static/image/other/pic.png"
				}
				this.talkList.push(data);

				this.$nextTick(() => {
					setTimeout(() => {
						uni.pageScrollTo({
							scrollTop: 9999, // 设置一个超大值，以保证滚动条滚动到底部
							duration: 0,
						});
					}, 1000)
				})

			},


		}
	}
</script>

<style lang="scss">
	@import "../../libs/global.scss";

	page {
		background-color: #F3F3F3;
		font-size: 28rpx;
	}

	.textType {
		text-decoration: underline;
		// border: 5rpx solid #F3F3F3;
	}

	/* 加载数据提示 */
	.tips {
		position: fixed;
		left: 0;
		top: var(--window-top);
		width: 100%;
		z-index: 9;
		background-color: rgba(0, 0, 0, 0.15);
		height: 72rpx;
		line-height: 72rpx;
		transform: translateY(-80rpx);
		transition: transform 0.3s ease-in-out 0s;

		&.show {
			transform: translateY(0);
		}
	}

	.box-1 {
		width: 100%;
		height: auto;
		padding-bottom: 100rpx;
		box-sizing: content-box;
		overflow-y: auto;

		/* 兼容iPhoneX */
		margin-bottom: 0;
		margin-bottom: constant(safe-area-inset-bottom);
		margin-bottom: env(safe-area-inset-bottom);
	}

	.box-2 {
		position: fixed;
		left: 0;
		width: 100%;
		bottom: -40px;
		height: auto;
		z-index: 2;
		border-top: #e5e5e5 solid 1px;
		box-sizing: content-box;
		background-color: #F3F3F3;


		/* 兼容iPhoneX */
		padding-bottom: 0;
		padding-bottom: constant(safe-area-inset-bottom);
		padding-bottom: env(safe-area-inset-bottom);

		>view {
			padding: 0 20rpx;
			height: 100rpx;
		}

		.content {
			background-color: #fff;
			height: 64rpx;
			padding: 0 20rpx;
			border-radius: 32rpx;
			font-size: 28rpx;
		}

		.send {
			background-color: #42b983;
			color: #fff;
			height: 64rpx;
			margin-left: 20rpx;
			border-radius: 32rpx;
			padding: 0;
			width: 120rpx;
			line-height: 62rpx;

			&:active {
				background-color: #5fc496;
			}
		}
	}

	.talk-list {
		padding-bottom: 20rpx;

		/* 消息项，基础类 */
		.item {
			padding: 20rpx 20rpx 0 20rpx;
			align-items: flex-start;
			align-content: flex-start;
			color: #333;

			.pic {
				width: 92rpx;
				height: 92rpx;
				border-radius: 50%;
				border: #fff solid 1px;
			}

			.content {
				padding: 20rpx;
				border-radius: 4px;
				max-width: 500rpx;
				word-break: break-all;
				line-height: 52rpx;
				position: relative;

				.hava-possible-issues {
					margin-top: 10rpx;
					width: 100%;

					.divider {
						width: 100%;
						height: 5rpx;
						background-color: #42B983;
					}

					.title {

						color: #42B983;

					}

					.issues-item {
						width: 100%;
						overflow: hidden;
						text-overflow: ellipsis;
						margin-bottom: 5rpx;
						color: #909399;
					}

					.symptom-item {
						width: 100%;
						padding-bottom: 5px;
						color: #909399;
					}
				}
			}

			/* 收到的消息 */
			&.pull {
				.content {
					margin-left: 32rpx;
					background-color: #fff;

					&::after {
						content: '';
						display: block;
						width: 0;
						height: 0;
						border-top: 16rpx solid transparent;
						border-bottom: 16rpx solid transparent;
						border-right: 20rpx solid #fff;
						position: absolute;
						top: 30rpx;
						left: -18rpx;
					}
				}
			}

			/* 发出的消息 */
			&.push {
				/* 主轴为水平方向，起点在右端。使不修改DOM结构，也能改变元素排列顺序 */
				flex-direction: row-reverse;

				.content {
					margin-right: 32rpx;
					background-color: #a0e959;

					&::after {
						content: '';
						display: block;
						width: 0;
						height: 0;
						border-top: 16rpx solid transparent;
						border-bottom: 16rpx solid transparent;
						border-left: 20rpx solid #a0e959;
						position: absolute;
						top: 30rpx;
						right: -18rpx;
					}
				}
			}
		}
	}
</style>