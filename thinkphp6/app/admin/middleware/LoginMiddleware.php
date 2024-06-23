<?php
declare (strict_types=1);

namespace app\admin\middleware;

use app\admin\models\UserModel;
use app\admin\util\JwtUtil;
use app\Request;
use think\facade\Cache;

class LoginMiddleware
{
    public function handle($request, \Closure $next)
    {
        // 添加中间件执行代码
        //解决跨域代码
        header("Access-Control-Allow-Origin: *");
        header('Access-Control-Allow-Headers:x-requested-with, content-type,token');
        header('Access-Control-Allow-Methods:POST,GET');
        header("Access-Control-Allow-Credentials", true);
        if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
            exit();
        }


        $token = $request->header("token");
        if (empty($token)) {
            return fail("登录失效", 201);
        }
        $decode = JwtUtil::decode($token, config('jwtConfig.secretKey'));
        if ($decode['code'] != 200) {
            return fail("登录失效", 201);
        }
        $user_id = $decode['data']->uid;
        $request->uid = $user_id;
        $cacheToken = $user_id . "token";
        $token1 = Cache::get($cacheToken);
        if (empty($token1)) {
            return fail("登录失效！", 201);
        }
        if ($token != $token1) {
            return fail("账号在其他地方登录！", 201);
        }


//        $toArray = UserModel::getUserPerm($decode['data']->uid);
//        $arr=[];
//        foreach ($toArray as $value){
//            array_push($arr,$value["perm"]);
//        }
//        $cachePerm = $decode['data']->uid."perm";
//        $arr = Cache::get($cachePerm);//以秒为单位
//        Request()->controller();//获取控制器名
//        Request()->action();//获取方法名
//        $str = Request()->controller() . "/" . Request()->action();
//        if(!in_array($str,$arr,true)){
//            return fail("没有该权限",202);
//        }
        return $next($request);
    }
}
