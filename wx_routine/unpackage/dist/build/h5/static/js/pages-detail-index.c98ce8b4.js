(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-detail-index"],{"01df":function(t,a,i){"use strict";i.r(a);var e=i("e8a6"),n=i("574e");for(var s in n)["default"].indexOf(s)<0&&function(t){i.d(a,t,(function(){return n[t]}))}(s);i("153b");var l=i("f0c5"),v=Object(l["a"])(n["default"],e["b"],e["c"],!1,null,"9a06b628",null,!1,e["a"],void 0);a["default"]=v.exports},"153b":function(t,a,i){"use strict";var e=i("7bae"),n=i.n(e);n.a},"574e":function(t,a,i){"use strict";i.r(a);var e=i("8927"),n=i.n(e);for(var s in e)["default"].indexOf(s)<0&&function(t){i.d(a,t,(function(){return e[t]}))}(s);a["default"]=n.a},"6dc2":function(t,a){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAABIhJREFUeF7tW0tS20AQfeJzjqCTYE4C3mkRpyoncDhBqnAW2mFOgnMSmXMEotRoJCGP5tPdM5KpGC1Bmpl+/fo/znDiT3bi8uMTgE8GnDgCs5hA8bO6wgXuGqwzfEGNqxb3BWrs27/vkWGPGi/qb+W3fDuHbiYDYCD0NYAFWxgFjAbkCW/Yld9zDVTiJzkAxaZSWn1E1ms5zZE1IMtyle/SLKhXSQZAq/FHkbY5EmXY4g/uUzEiGoBG8EusUbc2zhFG+q5mw1O5yn9Il+i+iwKgoTvwHHsI8fcKiDfcxLBBDEDxUN0hg6L8cZ9IEEQAFJtKUW99XMkHu0eYBBuADyf8UAs1ltz8gQXA0W0+RDlBqCQD8OGF78Bh+gQSAG2Mr0IKYP5/h1csm2/O8Zw0cdKpdE45Dw2ATaVCHT+d9ZygXOX93pMATPQHQQAmov69mcQUqUEmsoACwKTa70gyCQsybMuvuTYzx+MFYC7t9yBMwIJQphgCYBbtH5MFIQBqiidlvHNg+w3tAQxz+bl9gROAKXL9oedXghe/qkfVARo6xInM7sbVR3ADkNoegbH2L6Bzi1fkByzQwOgWWppnFHW6ZX0A8OnftbGA3+0GKtnZ28rVVvudkOOw2JoHztv84wzXbS+Rn494QqIVACb9d6pvxylCrCHPYIFP8c33Gpg1OYN0rJ8CAKd9uYRwODonTT3rcMpy6zntAPDqfRIADavUk+HWmVarfp/qAmu/YDWdIRhMpjIA4DmhXbnKb0wtNX2DGrdkitrU/O5TFDsOusGtGXCKKCvDXAzgJkB2EHhA2pluSWeFHWgGAA9Vxdacw9Ma3p4X1NIJr0zPWhekYoAWLCUIlnI2qmCaBQAfCLzEyp4XdIkTj0fd2wwTiLVdCxNYKa6ZGerhalxHytEgSREG7fowQGDR1wRgU/GzUvNULABSDD0Mm2O1000AJE7ZBICVCaYYecUAYGgrRYlsVqLTFEND1ENC1FiquT8ucNVkh3+x6ENvDHg2g/S0xtzVYKwjdNux1Rv3U2YNxH6YXTJT3jEEng6xrxyOmvyO2t6XWIcalOrkbbRYJG2SeCpNNwAxoYfYkqaGc1YEMRcNdIb9PUGpGRDa0T3l1YEJNz4KaSQIDEj8AMhZ4KztrTdK2vE2XrF1XXYQRQICEymDEU7TwZl2Dm6Nue8VeOb8wqIq2KsIAyBhwQB5kuDjrO3gDpDQB1hL9LGLIHgiURh6b2bwm5jdmeLWCGpfN6iIj5CCxNWTv0buL9IB0KYw/T3AeCxI1A+mwrZzCPpw8eLwVmAJzzKB7hxCh8QTQ/I2IeTZywTBZh+OCULhRQw4YELquz0CZQBg0364DdkJOn2C/h3AsS5Nkr29C9soAHo26KkPfU4n0/T7V8yrcL7tkgCgNugzvthpkO+0gouQIayTAWBECcUI2S9FbCeOuAs8OwDDDfsxtm8g6hL4DGrsfnB7JCSM5P/JGeA6RHcfqOkBdj+a0pceXppvuryfMBWWCDqpE0x5oLnXmo0BcwtG3e8TACpS/+t7J8+Af2Gmol+MpSS2AAAAAElFTkSuQmCC"},"7bae":function(t,a,i){var e=i("e43e");e.__esModule&&(e=e.default),"string"===typeof e&&(e=[[t.i,e,""]]),e.locals&&(t.exports=e.locals);var n=i("4f06").default;n("e0e45d28",e,!0,{sourceMap:!1,shadowMode:!1})},8927:function(t,a,i){"use strict";i("7a82"),Object.defineProperty(a,"__esModule",{value:!0}),a.default=void 0;var e=i("a295"),n=i("b687"),s=(i("f5aa"),{data:function(){return{isAdd:"",herbal_data:[],prescription_data:[],checkList:!1}},computed:{baseURL:function(){return n.baseURL}},onLoad:function(t){this.isAdd=t.value,1==this.isAdd?this.prescription_data=JSON.parse(decodeURIComponent(t.data)):this.herbal_data=JSON.parse(decodeURIComponent(t.data))},methods:{favClick:function(t){var a=this.prescription_data.id||this.herbal_data.id;(0,e.managerSc)({sc:a}).then((function(t){0==t.code&&uni.$u.toast("收藏成功")}))}}});a.default=s},a295:function(t,a,i){"use strict";i("7a82");var e=i("4ea4").default;Object.defineProperty(a,"__esModule",{value:!0}),a.managerSc=function(t){return(0,n.default)({url:"/admin/manager/sc",method:"post",data:t})};var n=e(i("e039"))},e43e:function(t,a,i){var e=i("24fb");a=e(!1),a.push([t.i,'@charset "UTF-8";\r\n/* uni.scss */\r\n/**\r\n * 这里是uni-app内置的常用样式变量\r\n *\r\n * uni-app 官方扩展插件及插件市场（https://ext.dcloud.net.cn）上很多三方插件均使用了这些样式变量\r\n * 如果你是插件开发者，建议你使用scss预处理，并在插件代码中直接使用这些变量（无需 import 这个文件），方便用户通过搭积木的方式开发整体风格一致的App\r\n *\r\n */\r\n/**\r\n * 如果你是App开发者（插件使用者），你可以通过修改这些变量来定制自己的插件主题，实现自定义主题功能\r\n *\r\n * 如果你的项目同样使用了scss预处理，你也可以直接在你的 scss 代码中使用如下变量，同时无需 import 这个文件\r\n */\r\n/* 颜色变量 */\r\n/* 行为相关颜色 */\r\n/* 文字基本颜色 */\r\n/* 背景颜色 */\r\n/* 边框颜色 */\r\n/* 尺寸变量 */\r\n/* 文字尺寸 */\r\n/* 图片尺寸 */\r\n/* Border Radius */\r\n/* 水平间距 */\r\n/* 垂直间距 */\r\n/* 透明度 */\r\n/* 文章场景相关 */.content[data-v-9a06b628]{width:100%;height:100vh;overflow-y:auto}.content .image_view[data-v-9a06b628]{width:100%;height:%?5000?%;position:absolute;z-index:-1;left:0;right:0;bottom:0;right:0;width:100%;height:100%}.content .picture[data-v-9a06b628]{aspect-ratio:16/9;width:100%}.content .picture uni-image[data-v-9a06b628]{aspect-ratio:16/9;width:100%;display:block}.content .text[data-v-9a06b628]{padding:16px}.content .text .icon[data-v-9a06b628]{width:%?45?%;height:%?45?%}.content .text .name[data-v-9a06b628]{font-size:28px;padding-bottom:16px;border-bottom:1px solid #e6e6e6}.content .text .herbal[data-v-9a06b628]{display:flex;justify-content:space-between}.content .text .herbal[data-v-9a06b628] :last-child{display:flex;align-items:center}.content .text .detail[data-v-9a06b628]{display:flex;justify-content:space-between}.content .text .detail[data-v-9a06b628] :last-child{display:flex;align-items:center}.content .text .names[data-v-9a06b628]{font-size:23px;padding-bottom:16px;padding-top:16px}.content .text .all_detail[data-v-9a06b628]{margin-top:16px}.content .text .all_detail .all_detail_text[data-v-9a06b628]{width:100%;word-wrap:break-word}.content .text .all_detail .all_detail_ul[data-v-9a06b628]{margin-top:32px;width:100%}.content .text .all_detail .all_detail_ul .li[data-v-9a06b628]{display:flex;padding-bottom:5px}.content .text .all_detail .all_detail_ul .li .li_name[data-v-9a06b628]{width:25%;margin-right:10%;word-wrap:break-word}.content .text .all_detail .all_detail_ul .li .li_answer[data-v-9a06b628]{width:75%;word-wrap:break-word}.content .interval[data-v-9a06b628]{width:100%;height:.08rem;background-color:#f5f5f5}',""]),t.exports=a},e8a6:function(t,a,i){"use strict";i.d(a,"b",(function(){return e})),i.d(a,"c",(function(){return n})),i.d(a,"a",(function(){}));var e=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("v-uni-view",{staticClass:"content"},[e("v-uni-image",{staticClass:"image_view",attrs:{src:"https://axy-uni.oss-cn-beijing.aliyuncs.com/1ABAFAAFDEDEF426F65BAC069C2D6370.jpg"}}),2==t.isAdd?e("v-uni-view",[e("v-uni-view",{staticClass:"picture"},[e("v-uni-view",[e("v-uni-image",{attrs:{src:t.baseURL+"/"+t.herbal_data.picture_path}})],1)],1),e("v-uni-view",{staticClass:"text"},[e("v-uni-view",{staticClass:"name,herbal"},[e("v-uni-view",[t._v(t._s(t.herbal_data.name))]),e("v-uni-view",[e("v-uni-image",{staticClass:"icon",attrs:{src:i("6dc2")}}),e("v-uni-text",{staticClass:"cText",staticStyle:{"font-size":"30rpx"},on:{click:function(a){arguments[0]=a=t.$handleEvent(a),t.favClick()}}},[t._v("收藏")])],1)],1),e("v-uni-view",{staticClass:"all_detail"},[e("v-uni-view",{staticClass:"all_detail_text"},[t._v(t._s(t.herbal_data.name+"，中药名。功效有"+t.herbal_data.effect+"药性"+t.herbal_data.property))]),e("v-uni-view",{staticClass:"all_detail_ul"},[e("v-uni-view",{staticClass:"li"},[e("v-uni-view",{staticClass:"li_name"},[t._v("中文名")]),e("v-uni-view",{staticClass:"li_answer"},[t._v(t._s(t.herbal_data.name))])],1),e("v-uni-view",{staticClass:"li"},[e("v-uni-view",{staticClass:"li_name"},[t._v("别名")]),e("v-uni-view",{staticClass:"li_answer"},[t._v(t._s(t.herbal_data.surname))])],1)],1)],1)],1),e("v-uni-view",{staticClass:"interval"}),e("v-uni-view",{staticClass:"text"},[e("v-uni-view",{staticClass:"names"},[t._v("药材功效")]),e("v-uni-view",{staticClass:"all_detail"},[e("v-uni-view",{staticClass:"all_detail_text"},[t._v(t._s(t.herbal_data.effect))])],1)],1),e("v-uni-view",{staticClass:"interval"}),e("v-uni-view",{staticClass:"text"},[e("v-uni-view",{staticClass:"names"},[t._v("药性")]),e("v-uni-view",{staticClass:"all_detail"},[e("v-uni-view",{staticClass:"all_detail_text"},[t._v(t._s(t.herbal_data.property))])],1)],1),e("v-uni-view",{staticClass:"interval"}),e("v-uni-view",{staticClass:"text"},[e("v-uni-view",{staticClass:"names"},[t._v("注意事项")]),e("v-uni-view",{staticClass:"all_detail"},[e("v-uni-view",{staticClass:"all_detail_text"},[t._v(t._s(t.herbal_data.manage))])],1)],1)],1):e("v-uni-view",[e("v-uni-view",{staticClass:"text"},[e("v-uni-view",{staticClass:"name,detail"},[e("v-uni-view",{},[t._v(t._s(t.prescription_data.name))]),e("v-uni-view",[e("v-uni-text",{staticStyle:{"font-size":"30rpx"},on:{click:function(a){arguments[0]=a=t.$handleEvent(a),t.favClick()}}},[t._v("收藏")])],1)],1),e("v-uni-view",{staticClass:"all_detail"},[e("v-uni-view",{staticClass:"all_detail_ul"},[e("v-uni-view",{staticClass:"li"},[e("v-uni-view",{staticClass:"li_name"},[t._v("出处")]),e("v-uni-view",{staticClass:"li_answer"},[t._v(t._s(t.prescription_data.provenance))])],1),e("v-uni-view",{staticClass:"li"},[e("v-uni-view",{staticClass:"li_name"},[t._v("功效")]),e("v-uni-view",{staticClass:"li_answer"},[t._v(t._s(t.prescription_data.effect))])],1),e("v-uni-view",{staticClass:"li"},[e("v-uni-view",{staticClass:"li_name"},[t._v("治疗症状")]),e("v-uni-view",{staticClass:"li_answer"},[t._v(t._s(t.prescription_data.major))])],1)],1)],1)],1),e("v-uni-view",{staticClass:"interval"}),e("v-uni-view",{staticClass:"text"},[e("v-uni-view",{staticClass:"names"},[t._v("治疗疾病以及注意事项")]),e("v-uni-view",{staticClass:"all_detail"},[e("v-uni-view",{staticClass:"all_detail_text"},[t._v(t._s(t.prescription_data.name+t.prescription_data.manage))])],1)],1),e("v-uni-view",{staticClass:"text"},[e("v-uni-view",{staticClass:"names"},[t._v("用法用量")]),e("v-uni-view",{staticClass:"all_detail"},[e("v-uni-view",{staticClass:"all_detail_text"},[t._v(t._s(t.prescription_data.compose))])],1)],1)],1)],1)},n=[]}}]);