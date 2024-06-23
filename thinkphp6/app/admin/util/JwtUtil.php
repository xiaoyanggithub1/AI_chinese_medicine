<?php

// +----------------------------------------------------------------------
// | JWT接口认证工具
// +----------------------------------------------------------------------

namespace app\admin\util;

use \Firebase\JWT\JWT;
use Firebase\JWT\Key;

class JwtUtil
{

    /**
     * Notes:jwt签发
     * User: 陆小会
     * DateTime: 2021/8/6 14:43
     * @param $uid 用户id
     * @param $key 秘钥
     * @param float|int $exp 过期时间，按秒
     * @return array
     */
    public static function encode($uid, $key,$exp=60*60*24*1000)
    {
        // 载荷部分
        $jwtData = [
            "iss" => '流笙', // 签发者
            'iat' =>time(), // 签发时间
            'uid' => $uid, // 用户ID
            'nbf' => time(), // TOKEN开始生效时间
            'exp' => time()+$exp, // TOKEN过期时间

        ];
        $jwtToken = JWT::encode($jwtData, $key, "HS256"); // TOKEN
        return ['access_token' => $jwtToken];
    }

    /**
     * Notes:jwt解密
     * User: 陆小会
     * DateTime: 2021/8/6 14:44
     * @param $token jwt
     * @param $key 秘钥
     * @return array
     */
    public static function decode($token, $key)
    {
        try {
            JWT::$leeway = 60; // 当前时间减去60秒，留点余地
            return ['code' => 200, 'data' => JWT::decode($token,new Key($key, 'HS256'))]; // HS256方式，这里要和token签发的时候对应
        } catch (\Firebase\JWT\SignatureInvalidException $e) {
            // 无效Token
            return ['code' => 10001, 'msg' => '无效的Token'];
        } catch (\Firebase\JWT\BeforeValidException $e) {
            // Token在某个时间点之后才能用
            return ['code' => 10002, 'msg' => 'Token不在使用时间区间'];
        } catch (\Firebase\JWT\ExpiredException $e) {
            // Token已过期
            return ['code' => 10003, 'msg' => 'Token已过期'];
        } catch (\Exception $e) {
            // 其他错误
            return ['code' => 10001, 'msg' => '无效的Token'];
        }
    }
}
