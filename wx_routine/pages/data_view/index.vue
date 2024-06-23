<template>
	<view class="content">
		<view class="headInput">
			<u-search :show-action="true" action-text="搜索" :animation="true"></u-search>
		</view>
		<view id="main">
			<view class="data_aggregates">
				<view class="chart_title">
					智能问诊系统数据总汇
				</view>
				<qiun-data-charts type="column" :opts="column_opts" :chartData="column_chartData" />
			</view>
			<view class="proportion_of_data">
				<view class="chart_title">
					智能问诊系统数据占比
				</view>
				<qiun-data-charts type="pie" :opts="pie_opts" :chartData="pie_chartData" />
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				column_chartData: {},
				pie_chartData: {},
				//您可以通过修改 config-ucharts.js 文件中下标为 ['column'] 的节点来配置全局默认参数，如都是默认参数，此处可以不传 opts 。实际应用过程中 opts 只需传入与全局默认参数中不一致的【某一个属性】即可实现同类型的图表显示不同的样式，达到页面简洁的需求。
				pie_opts: {
					color: ["#1890FF", "#91CB74", "#FAC858", "#EE6666", "#73C0DE", "#3CA272", "#FC8452", "#9A60B4",
						"#ea7ccc"
					],
					padding: [5, 5, 5, 5],
					enableScroll: false,
					extra: {
						pie: {
							activeOpacity: 0.5,
							activeRadius: 10,
							offsetAngle: 0,
							labelWidth: 15,
							border: false,
							borderWidth: 3,
							borderColor: "#FFFFFF"
						}
					}
				},
				column_opts: {
					color: ["#FAC858", "#EE6666", "#FAC858", "#EE6666", "#73C0DE", "#3CA272", "#FC8452", "#9A60B4",
						"#ea7ccc"
					],
					padding: [15, 15, 0, 5],
					enableScroll: false,
					legend: {},
					xAxis: {
						disableGrid: true
					},
					yAxis: {
						data: [{
							min: 0
						}]
					},
					extra: {
						column: {
							type: "group",
							width: 30,
							activeBgColor: "#000000",
							activeBgOpacity: 0.08,
							linearType: "custom",
							seriesGap: 5,
							linearOpacity: 0.5,
							barBorderCircle: true,
							customColor: [
								"#FA7D8D",
								"#EB88E2"
							]
						}
					}
				}
			};
		},
		onReady() {
			this.column_getServerData();
			this.pie_getServerData()
		},
		methods: {
			column_getServerData() {
				//模拟从服务器获取数据时的延时
				setTimeout(() => {
					//模拟服务器返回数据，如果数据格式和标准格式不同，需自行按下面的格式拼接
					let res = {
						categories: ["2018", "2019", "2020", "2021", "2022", "2023"],
						series: [{
								name: "方剂访问总量",
								data: [35, 36, 31, 33, 13, 34]
							},
							{
								name: "中药访问总量",
								data: [18, 27, 21, 24, 6, 28]
							}
						]
					};
					this.column_chartData = JSON.parse(JSON.stringify(res));
				}, 500);
			},
			pie_getServerData() {
				setTimeout(() => {
					let res = {
						series: [{
							data: [{
								"name": "疾病症状",
								"value": 45
							}, {
								"name": "并发疾病",
								"value": 30
							}, {
								"name": "疾病易吃食物",
								"value": 20
							}, {
								"name": "疾病推荐食物",
								"value": 18
							}, {
								"name": "疾病忌吃食物",
								"value": 13
							}]
						}]
					};
					this.pie_chartData = JSON.parse(JSON.stringify(res));
				}, 500);
			},
		}
	};
</script>


<style lang="scss" scoped>
	.content {
		background-color: $uni-bg-color-grey;
		height: 100vh;
		width: 100vw;
		position: relative;

		.headInput {
			padding: 5px;
			background-color: saddlebrown;
		}

		#main {
			height: calc(100vh - 52px);
			width: 100vw;
			overflow: auto;

			.data_aggregates {
				padding: 15px;
				margin-top: 20px;

				.chart_title {
					height: 30px;
					text-align: center;
				}
			}

			.proportion_of_data {
				padding: 15px;
				margin-top: 20px;

				.chart_title {
					height: 30px;
					text-align: center;
				}
			}
		}
	}
</style>