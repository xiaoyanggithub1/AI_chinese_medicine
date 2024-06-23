<!-- 蓝色简洁登录页面 -->
<template>

	<view class="t-login">
		<view class="img_box">
			<image src="https://axy-uni.oss-cn-beijing.aliyuncs.com/homeDoctor.png"></image>
		</view>
		

		<!-- 页面装饰图片  图片没哟-->
		<!-- 	<image class="img-a" src="@/static/image/other/2.png"></image>
		<image class="img-b" src="@/static/image/other/3.png"></image> -->

		<!-- 标题 -->
		<view class="t-b" style="font-size: 60rpx; color: #c6955d;">{{ title }}</view>
		<!-- -->
		<input style="font-size: 45rpx; background-color: lightgray;" type="text" placeholder="请输入账号" v-model="userInfo.loginForm.username">
		<input style="font-size: 45rpx; background-color: lightgrey;" type="password" placeholder="输入密码" v-model="userInfo.loginForm.password">

		<button type="primary" @click="login"><text v-if="isLogin">登录</text> <text v-else> 注册</text></button>



		<view class="t-f" @click="changForm"><text v-if="isLogin">————— 没有账号，去注册一个 —————</text>
			<text v-else>————— 已有账号，去登录 —————</text>
		</view>
		<!-- <view class="t-e cl">
			<view class="t-g" @tap="wxLogin()"><image src="@/static/image/other/wx.png"></image></view>
			<view class="t-g" @tap="zfbLogin()"><image src="@/static/image/other/qq.png"></image></view>
		</view> -->
	</view>
</template>
<script>
	import {
		loginManager,
		managers
	} from '@/api/login/index.js'

	import {
		getToken
	} from '@/utils/auth.js'

	export default {

		data() {
			return {
				title: 'AI中医馆', //填写logo或者app名称，也可以用：欢迎回来，看您需求
				second: 60, //默认60秒
				showText: true, //判断短信是否发送
				phone: '', //手机号码
				yzm: '', //验证码
				isLogin: true,

				// 登录表单
				userInfo: {
					loginForm: {
						username: '',
						password: ''
					},
				},
				// 登录表单验证规则

			};
		},
		onLoad() {
			const token = getToken()
			if (token) {
				this.$store.commit("SET_TOKEN", token)
				uni.redirectTo({
					url: '/pages/home/home'
				});
				
			}else{
				uni.$u.toast('请进行登录或注册！')
			}

		},
		onReady() {
			// this.$refs.loginForm.setRules(this.rules)
		},
		methods: {
			//当前登录按钮操作
			login() {
				// setTimeout(() => {
				// 	uni.switchTab({
				// 		url: '/pages/home/home'
				// 	});
				// }, 500)

				// return

				// 注册的验证
				if (this.userInfo.loginForm.username == '') {
					uni.$u.toast('用户名不能为空')
					return
				}
				if (!this.userInfo.loginForm.username.match(/^[a-zA-Z]\w{4,15}$/)) {
					uni.$u.toast('用户名需要字母开头，允许5-16字节')
					return

				}

				if (this.userInfo.loginForm.password == '') {
					uni.$u.toast('密码不能为空')
					return
				}

				if (!this.userInfo.loginForm.password.match(
						/^\S*(?=\S{6,})(?=\S*\d)(?=\S*[A-Z])(?=\S*[a-z])(?=\S*[!@#$%^&*? ])\S*$/)) {
					uni.$u.toast('密码最少6位，1个大小写字母，1个数字，1个特殊字符')
					return
				}
				if (this.isLogin) {
					this.$store.dispatch("Login", this.userInfo.loginForm).then(res => {

						uni.$u.toast('登录成功')

						setTimeout(() => {
							uni.switchTab({
								url: '/pages/home/home'
							});
						}, 500)

					}).catch(res => {
						uni.$u.toast(res.data)
					})
				} else {
					managers(this.userInfo.loginForm).then(res => {
						if (res.code == 0) {
							this.isLogin = true
							uni.$u.toast('注册成功')
						}
					}).catch(res => {
						uni.$u.toast(res.data)
					})
				}


			},

			logon() {

			},
			//注册表单切换事件
			changForm() {
				this.isLogin = !this.isLogin
				this.userInfo.loginForm = {
					username: '',
					password: ''
				}
			},
			//获取短信验证码
			getCode() {
				var that = this;
				var interval = setInterval(() => {
					that.showText = false;
					var times = that.second - 1;
					//that.second = times<10?'0'+times:times ;//小于10秒补 0
					that.second = times;
					console.log(times);
				}, 1000);
				setTimeout(() => {
					clearInterval(interval);
					that.second = 60;
					that.showText = true;
				}, 60000);
				//这里请求后台获取短信验证码
				uni.request({
					//......//此处省略
					success: function(res) {
						that.showText = false;
					}
				});
			},
			//等三方微信登录
			wxLogin() {
				uni.showToast({
					title: '微信登录',
					icon: 'none'
				});
			},
			//第三方支付宝登录
			zfbLogin() {
				uni.showToast({
					title: 'QQ登录',
					icon: 'none'
				});
			}
		}
	};
</script>
<style>
	.img-a {
		position: absolute;
		width: 100%;
		top: -280rpx;
		right: -100rpx;
	}

	.img-b {
		position: absolute;
		width: 50%;
		bottom: 0;
		left: -50rpx;
		margin-bottom: -200rpx;
	}

	.t-login {
		width: 600rpx;
		margin: 0 auto;
		font-size: 28rpx;
		color: #000;
		position: relative;
	}

	.t-login button {
		font-size: 28rpx;
		background: #c6955d;
		color: #fff;
		height: 90rpx;
		line-height: 90rpx;
		border-radius: 50rpx;
		box-shadow: 0 5px 7px 0 rgba(86, 119, 252, 0.2);
	}
	.img_box{
		/* position: ; */
	}

	.t-login input {
		padding: 0 20rpx 0 120rpx;
		height: 90rpx;
		line-height: 90rpx;
		margin-bottom: 50rpx;
		background: #f8f7fc;
		border: 1px solid #e9e9e9;
		font-size: 28rpx;
		border-radius: 50rpx;
	}

	.t-login .t-a {
		position: relative;
	}

	.t-login .t-a image {
		width: 40rpx;
		height: 40rpx;
		position: absolute;
		left: 40rpx;
		top: 28rpx;
		border-right: 2rpx solid #dedede;
		padding-right: 20rpx;
	}

	.t-login .t-b {
		text-align: left;
		font-size: 46rpx;
		color: #000;
		padding: 0rpx 0 120rpx 0;
		font-weight: bold;
	}

	.t-login .t-c {
		position: absolute;
		right: 22rpx;
		top: 22rpx;
		background: #c6955d;
		color: #fff;
		font-size: 24rpx;
		border-radius: 50rpx;
		height: 50rpx;
		line-height: 50rpx;
		padding: 0 25rpx;
	}

	.t-login .t-d {
		text-align: center;
		color: #999;
		margin: 80rpx 0;
	}

	.t-login .t-e {
		text-align: center;
		width: 250rpx;
		margin: 80rpx auto 0;
	}

	.t-login .t-g {
		float: left;
		width: 50%;
	}

	.t-login .t-e image {
		width: 50rpx;
		height: 50rpx;
	}

	.t-login .t-f {
		text-align: center;
		margin: 200rpx 0 0 0;
		color: #666;
	}

	.t-login .t-f text {
		margin-left: 20rpx;
		color: #aaaaaa;
		font-size: 27rpx;
	}

	.t-login .uni-input-placeholder {
		color: #000;
	}

	.cl {
		zoom: 1;
	}

	.userImage {
		position: absolute;
		top: 5%;
		bottom: 72%;
		left: 16%;
		width: 195rpx;
		height: 195rpx;
		overflow: hidden;
		border-radius: 50%;
		border: 2px solid white;
	}

	.cl:after {
		clear: both;
		display: block;
		visibility: hidden;
		height: 0;
		content: '\20';
	}
</style>