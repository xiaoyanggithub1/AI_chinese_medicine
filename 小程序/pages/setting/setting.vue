<template>
	<view>
		<!-- <view class="image_box">
			<image class="image"
				src="https://axy-uni.oss-cn-beijing.aliyuncs.com/eiffel-tower-paris-buildings-desktop-background-images.jpg">
			</image>
		</view> -->
		<view class="input_box">
			<input class="updateName" type="text" v-model="from.username" placeholder="请输入新的用户名" />
			<input class="updatePassword" type="password" v-model="from.password" placeholder="请输入新的密码" />
		</view>

		<view class="button_box">
			<button class="submit_box" form-type="submit" @click="submit()">提交</button>
			<!-- <button class="reset" form-type="reset" @click="reset()">重置</button> -->
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
				from: {
					username: '',
					password: ''

				}

			}
		},
		methods: {
			//提交函数
			submit() {
				if (this.from.username == '') {
					uni.$u.toast('用户名不能为空')
					return
				}
				if (!this.from.username.match(/^[a-zA-Z]\w{4,15}$/)) {
					uni.$u.toast('帐号不合法(字母开头，允许5-16字节，允许字母数字下划线组合')
					return

				}

				if (this.from.password == '') {
					uni.$u.toast('密码不能为空')
					return
				}

				if (!this.from.password.match(
						/^\S*(?=\S{6,})(?=\S*\d)(?=\S*[A-Z])(?=\S*[a-z])(?=\S*[!@#$%^&*? ])\S*$/)) {
					uni.$u.toast('密码不合法，最少6位，包括至少1个大写字母，1个小写字母，1个数字，1个特殊字符')
					return
				}

				updateManagers(this.from).then(res => {
					console.log(res)
					this.$store.commit("SET_TOKEN", '')
					removeToken()
					uni.$u.toast('密码修改成功，请重新登录！')

					setTimeout(() => {
						uni.redirectTo({
							url: '/pages/login/index'
						});
					}, 500)
				})
			},

			reset() {
				this.from = {
					username: '',
					password: ''
				}
			}

		}
	}
</script>


<style lang="scss">
	/* .image_box {
		width: 100%;

		.image {
			width: 100%;
		}
	} */

	.input_box {
		width: 90%;

		input {
			background: #E9E9EB;
			margin: 15rpx;
			padding: 10rpx;
			width: calc(100% - 20rpx);
			border-radius: 20rpx;
			height: 80rpx;
			

		}

	}

	.button_box {
		display: flex;
		flex-wrap: nowrap;
		justify-content: center;

		.submit_box {
			margin: 20rpx;
			width: 20%;
			height: 80rpx;
			background-color: #a9b8d5;
			text-align: center;
		}

		
	}
</style>