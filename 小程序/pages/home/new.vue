<template>
	<view class="app-container">
		<view class="container">
			<!-- <view class="title">
				新闻标题
			</view> -->
			<view class="rich">
				<rich-text :nodes='nodes' style="width: 100%;"></rich-text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				newId: 1,
				nodes: '内容1',



				// 内容
				nodeList: [{
						text: `<h1 style="margin: 0px auto; padding: 0px; text-align: center; line-height: 48px; font-size: 24px; color: rgb(1, 1, 1); font-family: 微软雅黑; white-space: normal;">安徽亳州谯城区风华桐乡路小学开展“中医药文化进校园”活动</h1>
<img src="https://axy-uni.oss-cn-beijing.aliyuncs.com/pic1%20anhui.jpg.crdownload" style="width:100%" alt="" srcset="">
<p><br/></p>
<p><br/></p>
<p><span style="color: rgb(72, 72, 72); font-family: 微软雅黑; text-indent: 32px;">4月27日，安徽省亳州市谯城区风华桐乡路小学开展“中医药文化进校园”活动，邀请当地执业中药师走进校园，开展中医药知识讲座、中药材辨识、使用中药戥子称量药材等活动，让小学生近距离感受中医药文化，激发学生学习中医药知识的兴趣。</span></p>
<p></p>
<p style="margin-top: 0px; margin-bottom: 12px; padding: 0px; color: rgb(72, 72, 72); font-family: 微软雅黑; white-space: normal; text-indent: 2rem;">图为执业中药师吴刘胜教学生使用戥子称量药材。</p>
<p style="margin-top: 0px; margin-bottom: 12px; padding: 0px; color: rgb(72, 72, 72); font-family: 微软雅黑; white-space: normal; text-indent: 2rem;"><span style="color: rgb(72, 72, 72); font-family: 微软雅黑; text-indent: 32px;">刘勤利 徐玲玲摄影报道</span></p>
<p><span style="color: rgb(72, 72, 72); font-family: 微软雅黑; text-indent: 32px;"></span><br/></p>`
					},
					{
						text: `<h1 style="margin: 0px auto; padding: 0px; text-align: center; line-height: 48px; font-size: 24px; color: rgb(1, 1, 1);  font-family: 微软雅黑; white-space: normal;">吉林省首届“阅读中华悦动青春”大学生读书节开幕</h1>
<img src="https://axy-uni.oss-cn-beijing.aliyuncs.com/pic2%20jilin.jpg.crdownload"  style="width:100%" alt="" srcset="">
<p style="margin-top: 0px; margin-bottom: 12px; padding: 0px; color: rgb(72, 72, 72); font-family: 微软雅黑; white-space: normal; text-indent: 2rem;">“阴阳者，天地之道也，万物之纲纪，变化之父母，生杀之本始，神明之府也，治病必求于本……”4月22日，在一段气势恢宏的《黄帝内经》诵读声中，吉林省首届“阅读中华悦动青春”大学生读书节在长春中医药大学拉开帷幕。活动由吉林省教育厅主办、长春中医药大学承办，向全省大学生了发出“爱读书、好读书、善读书”的号召。据悉，读书节将持续至今年10月，其间全省各高校将按照读书节活动方案继续举行不同形式的读书活动，进一步激发大学生阅读兴趣。</p>
<p style="margin-top: 0px; margin-bottom: 12px; padding: 0px; color: rgb(72, 72, 72); font-family: 微软雅黑; white-space: normal; text-indent: 2rem;">图为大学生们在诵读《黄帝内经》。本报记者许守年 李卓林 通讯员肖春崧摄影报道</p>
<p><br/></p>`
					},
					{
						text: `<h1 style="margin: 0px auto; padding: 0px; text-align: center; line-height: 48px; font-size: 24px; color: rgb(1, 1, 1);  font-family: 微软雅黑; white-space: normal;">湖南郴州市北湖实验学校学生在制作中药香囊</h1>
<img src="https://axy-uni.oss-cn-beijing.aliyuncs.com/pic3%20hunan.jpg.crdownload"  style="width:100%"  alt="" srcset="">
<p style="margin-top: 0px; margin-bottom: 12px; padding: 0px; color: rgb(72, 72, 72); font-family: 微软雅黑; white-space: normal; text-indent: 2rem;">4月17日，湖南省郴州市北湖实验学校组织学生前往郴州市香草中医药文化实践基地开展研学实践活动。在中医药文化展厅里，学生们了解了十大名医、九大体质、中医四诊等中医知识；在中草药植物科普园，大家了解郴州中草药的分布特点，辨识桑叶、金银花、菊花、蒲公英、山楂、合子草、益母草、石楠等中草药，并了解其基本功效；在中医药研发实验室，同学们手工制作“美容护肤精油皂”和“香草锦囊”等。</p>
<p style="margin-top: 0px; margin-bottom: 12px; padding: 0px; color: rgb(72, 72, 72); font-family: 微软雅黑; white-space: normal; text-indent: 2rem;">图为学生们在制作中药香囊。</p>
<p style="margin-top: 0px; margin-bottom: 12px; padding: 0px; color: rgb(72, 72, 72); font-family: 微软雅黑; white-space: normal; text-indent: 2rem;">彭临梦 周能军摄影报道</p>
<p><br/></p>`
					},
					{
						text: `<h1 style="margin: 0px auto; padding: 0px; text-align: center; line-height: 48px; font-size: 24px; color: rgb(1, 1, 1);  font-family: 微软雅黑; white-space: normal;">
    湖北省中医养生功法大赛决赛在武汉江滩举行</h1>
<img style='width:100%' src="https://axy-uni.oss-cn-beijing.aliyuncs.com/pic4%20hubei.jpg.crdownload" alt="" srcset="">
<p style="margin-top: 0px; margin-bottom: 12px; padding: 0px;"><br/></p>
<p style="margin-top: 0px; margin-bottom: 12px; padding: 0px; text-indent: 2rem;">近日，湖北省中医养生功法大赛决赛在武汉江滩举行，湖北各市州的12支代表队参加比赛，太极拳、太极剑、八段锦、五禽戏等传统功法一一亮相。本次活动由湖北省卫生健康委、省中医药管理局主办，省卫生健康宣传教育中心、武汉市卫生健康委联合承办，武汉市中医医院协办。图为大赛现场参赛队伍展示八段锦。本报讯记者毛旭 通讯员萧济康摄影报道</p>`
					}
				]

			}
		},
		onLoad(option) {
			this.newId = option.id
			this.nodes = this.nodeList[this.newId - 1].text
		},
		methods: {

		}
	}
</script>

<style lang="scss" scoped>
	.app-container {
		width: 100%;

		.container {
			padding: 20rpx;
			width: calc(100% - 40rpx);

			.title {
				width: 100%;
				text-align: center;
				font-size: 60rpx;
				margin-bottom: 50rpx;
			}

			.rich {
				width: 100%;
			}
		}
	}
</style>