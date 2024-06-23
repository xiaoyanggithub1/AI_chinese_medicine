<?php
// 应用公共文件
use think\facade\Request;

function success($data = null, $code = 0, $msg = 'ok'): \think\response\Json
{
    return json(['code' => $code, 'msg' => $msg, 'data' => $data, 'method' => request::method(), 'url' => request::baseUrl()]);
}

function fail($data = null, $code = 1, $msg = '请求失败！'): \think\response\Json
{
    return json(['code' => $code, 'msg' => $msg, 'data' => $data, 'method' => request::method(), 'url' => request::baseUrl()]);
}

function successs($data = null, $code = 0, $errno = 0): \think\response\Json
{
    return json(['code' => $code, 'errno' => $errno, 'data' => $data, 'method' => request::method(), 'url' => request::baseUrl()]);
}

function faill($data = null, $code = 0, $errno = 1): \think\response\Json
{
    return json(['code' => $code, 'errno' => $errno, 'data' => $data, 'method' => request::method(), 'url' => request::baseUrl()]);
}
