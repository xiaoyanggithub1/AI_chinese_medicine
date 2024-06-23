<template>
	<view class="page-main">
		<view class="search-header">
			<image class="search-img" src="../../static/search.png"></image>
			<input class="search-input" type="text" v-if="isAdd==1" v-model.trim="searchText" @confirm="confirmSearch"
				@input="inputSearch" placeholder-class="placeholder-name" placeholder="请输入方剂名称" />
			<input class="search-input" type="text" v-else v-model.trim="searchText_herbal" @confirm="confirmSearch"
				@input="inputSearch" placeholder-class="placeholder-name" placeholder="请输入中药名称" />
			<view class="search-name" @click="confirmSearch">搜索</view>
		</view>

		<!-- 历史记录 -->
		<view class="" v-if="isAdd==1">
			<view class="search-history" v-if="historyList.length">
				<view class="history-title">
					<view class="title-name">搜索历史</view>
					<image class="title-img" src="https://axy-uni.oss-cn-beijing.aliyuncs.com/delete.png"
						@click="deleteAll"></image>
				</view>
				<view class="history-list">
					<view class="history-name" :style="isDelete?'padding:0 32rpx 0 16rpx;':''"
						v-for="(item,index) in historyList" :key="index" @click="clickHis(item,index)">
						{{item}}
						<span class="delete-icon" v-if="isDelete">x</span>
					</view>
				</view>
			</view>
		</view>
		<view class="" v-else>
			<view class="search-history" v-if="historyListHerbal.length">
				<view class="history-title">
					<view class="title-name">搜索历史</view>
					<image class="title-img" src="https://axy-uni.oss-cn-beijing.aliyuncs.com/delete.png"
						@click="deleteAll"></image>
				</view>
				<view class="history-list">
					<view class="history-name" :style="isDelete?'padding:0 32rpx 0 16rpx;':''"
						v-for="(item,index) in historyListHerbal" :key="index" @click="clickHis(item,index)">
						{{item}}
						<span class="delete-icon" v-if="isDelete">x</span>
					</view>
				</view>
			</view>
		</view>
		<view class="search-history" v-if="hotList.length">
			<view class="history-title">
				<view class="title-name">热门搜索</view>
				<!-- <image src="../../static/see.png" class="title-img"></image> -->
			</view>
			<view class="history-list" v-if="seeMore">
				<view class="history-name" v-for="(item,index) in hotList" :key="index" @click="clickHis(item)">
					{{item}}
				</view>
			</view>
		</view>
	</view>
</template>
<script>
	
	import {
		cxzhongyao,
		cxfangji
	} from "../../api/intelligent.js"
	export default {

		data() {
			return {
				searchImg: '',
				// 方剂1
				historyList: [],
				// 中药2
				historyListHerbal: [],
				searchText: '', //搜索内容
				searchText_herbal: "",
				seeMore: true,
				isDelete: false,
				hotList: [
					"当归", "决明子"
				],
				isAdd: ""
			}
		},

		onLoad: function(option) {
			this.isAdd = option.value
			console.log("onLoad");
			if (this.isAdd == 1) {
				uni.setNavigationBarTitle({
					title: '方剂查询'
				});
			} else {
				uni.setNavigationBarTitle({
					title: '中药查询'
				});
			}
		},

		onReady() {
			// console.log(uni.getStorageSync('liu-search-name-list'),'xxx')
			if (uni.getStorageSync('liu-search-name-list')) {
				this.historyList = uni.getStorageSync('liu-search-name-list').reverse()
			} else {
				this.historyList = []
			}
			if (uni.getStorageSync('liu-search-name-list-herbal')) {
				this.historyListHerbal = uni.getStorageSync('liu-search-name-list-herbal').reverse()
			} else {
				this.historyListHerbal = []
			} // this.historyListHerbal = uni.getStorageSync('liu-search-name-list-herbal').reverse() || []
		},

		methods: {
			//全部删除
			deleteAll() {
				if (this.isAdd == 1) {
					uni.setStorageSync('liu-search-name-list', '')
					this.historyList = []
				} else {
					uni.setStorageSync('liu-search-name-list-herbal', '')
					this.historyListHerbal = []
				}
			},
			//点击热门搜索
			// deBug
			clickHis(name, index) {
				if (this.isAdd == 1) {
					if (this.isDelete) {
						this.historyList.splice(index, 1)
						uni.setStorageSync('liu-search-name-list', this.historyList)
					} else {
						this.searchText = name
						this.confirmSearch()
					}
				} else {
					if (this.isDelete) {
						this.historyListHerbal.splice(index, 1)
						uni.setStorageSync('liu-search-name-list-herbal', this.historyListHerbal)
					} else {
						this.searchText_herbal = name
						this.confirmSearch()
					}
				}
			},
			//搜索框输入事件
			inputSearch() {
				if (this.isAdd == 1) {
					this.$emit('input', this.searchText)
				} else {
					this.$emit('input', this.searchText_herbal)
				}
			},
			//搜索
			confirmSearch() {
				if (this.isAdd == 1) {
					let oldList = uni.getStorageSync('liu-search-name-list') || []
					let hasName = false
					let data_prescription = {
						name: this.searchText
					}
					console.log(data_prescription);
					cxfangji(data_prescription).then((res) => {
						console.log(res);
						if (res.data.code == 0 && res.data.data != '当前方剂不存在') {
							uni.navigateTo({
								url: '../detail/index?value=1&data=' + encodeURIComponent(JSON.stringify(
									res.data.data))
							});
						} else {
							uni.$u.toast('当前方剂不存在')
						}
					})
					console.log(this.searchText);
					oldList.forEach(res => {
						if (res == this.searchText) hasName = true
					})
					if (!hasName && this.searchText) {
						oldList.push(this.searchText)
						uni.setStorageSync('liu-search-name-list', oldList)
						this.historyList = uni.getStorageSync('liu-search-name-list').reverse() || []
					}
					this.$emit('change', this.searchText)
				} else {
					let oldList = uni.getStorageSync('liu-search-name-list-herbal') || []
					let hasName = false
					let data_herbal = {
						name: this.searchText_herbal
					}
					console.log(data_herbal);
					cxzhongyao(data_herbal).then((res) => {
						console.log(res);
						if (res.data.code == 0 && res.data.data != '当前中药不存在') {
							console.log("dhfjdfkdf");
							uni.navigateTo({
								url: '../detail/index?value=2&data=' + encodeURIComponent(JSON.stringify(
									res.data.data))
							});
						} else {
							uni.$u.toast('当前中药不存在')
						}
					})
					oldList.forEach(res => {
						if (res == this.searchText_herbal) hasName = true
					})
					if (!hasName && this.searchText_herbal) {
						oldList.push(this.searchText_herbal)
						uni.setStorageSync('liu-search-name-list-herbal', oldList)
						console.log(uni.getStorageSync('liu-search-name-list-herbal'));
						this.historyListHerbal = uni.getStorageSync('liu-search-name-list-herbal').reverse() || []
					}
					this.$emit('change', this.searchText_herbal)

				}
			}
		}
	}
</script>
<style lang="scss" scoped>
	page {
		background-color: #f8f8f8;
	}

	.page-main {
		width: 100%;
		height: 100vh;
		display: inline-block;

		.search-header {
			width: calc(100%-64rpx);
			padding: 0 32rpx;
			height: 112rpx;
			display: flex;
			align-items: center;
			justify-content: space-between;
			position: relative;

			.search-img {
				position: absolute;
				left: 64rpx;
				width: 32rpx;
				height: 32rpx;
			}

			.search-input {
				padding: 0 32rpx 0 76rpx;
				width: calc(90% - 108rpx);
				height: 72rpx;
				line-height: 72rpx;
				background-color: #F2F3F5;
				border: solid #e4e4e5 1rpx;
				border-radius: 36rpx;
				font-size: 30rpx;
				color: #666666;
			}

			.placeholder-name {
				font-size: 30rpx;
				color: #999999;
			}

			.search-name {
				width: 80rpx;
				text-align: right;
				font-size: 30rpx;
				color: #666666;
			}
		}

		.search-history {
			padding: 0 20rpx;
			margin-top: 24rpx;

			.history-title {
				display: flex;
				align-items: center;
				justify-content: space-between;

				.title-name {
					font-size: 30rpx;
					color: #666666;
					font-weight: bold;
					margin-left: 12rpx;
				}

				.title-img {
					width: 34rpx;
					height: 34rpx;
					margin-right: 12rpx;
				}

				.history-delete {
					height: auto;
					display: flex;
					align-items: center;
					justify-content: flex-end;

					.delete-all {
						font-size: 26rpx;
						color: #666666;
					}

					.delete-line {
						width: 1px;
						height: 20rpx;
						background-color: #999999;
						margin: 0 12rpx;
					}

					.delete-complete {
						font-size: 26rpx;
						color: #F71E1E;
					}
				}
			}

			.history-list {
				width: 100%;
				display: flex;
				align-items: flex-start;
				justify-content: flex-start;
				flex-wrap: wrap;
				padding: 12rpx 0;

				.history-name {
					height: 48rpx;
					line-height: 48rpx;
					padding: 0 24rpx;
					background-color: #FFFFFF;
					border-radius: 25rpx;
					display: flex;
					align-items: center;
					justify-content: center;
					margin: 10rpx 12rpx;
					font-size: 26rpx;
					color: #666666;
					overflow: hidden;
					text-overflow: ellipsis;
					display: -webkit-box;
					-webkit-box-orient: vertical;
					-webkit-line-clamp: 1; //控制显示的行数
					position: relative;

					.delete-icon {
						position: absolute;
						font-size: 26rpx;
						color: #e4e4e5;
						right: 12rpx;
						bottom: 2rpx;
					}
				}
			}
		}
	}
</style>