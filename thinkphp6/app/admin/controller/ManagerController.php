<?php


namespace app\admin\controller;


use app\admin\models\FJModel;
use app\admin\models\ManagerModel;
use app\admin\models\ManagerRoleModel;
use app\admin\models\MenuModel;
use app\admin\models\PictureModel;
use app\admin\models\RoleMenuModel;
use app\admin\models\RoleModel;
use app\admin\models\SCModel;
use app\admin\models\UserRoleModel;
use app\admin\models\YJModel;
use app\admin\models\ZYModel;
use app\admin\util\JwtUtil;
use app\admin\validate\UserValidate;
use app\BaseController;
use think\facade\Cache;
use think\Model;

class ManagerController extends BaseController
{
    //管理员新增

    public function managers()
    {
        $data = input('post.');
        try {
            validate(UserValidate::class)->scene('new')->check($data);
        } catch (\Exception $e) {
            // 验证失败 输出错误信息
            return success($e->getError());
        }
        $managerModel = ManagerModel::where("username", $data['username'])->find();
        if (!empty($managerModel)) {
            return fail('账号已存在，请重新注册');
        }
        $data['password'] = md5($data['password']);
        $managerModel = new ManagerModel();//实例化
        $managerModel->save($data);

        return success("注册成功！");
    }

    public function updateManagers()
    {
        $data = input("post.");
        $id = request()->uid;
        try {
            validate(UserValidate::class)->scene('new')->check($data);
        } catch (\Exception $e) {
            // 验证失败 输出错误信息
            return success($e->getError());
        }

        $managerModel = ManagerModel::find($id);


        if ($managerModel['username'] != $data['username']) {
            $managerModel1 = ManagerModel::where("username", $data["username"])->find();
            if (!empty($managerModel1)) {
                return fail("账号已存在，请更换用户名！");
            }
        }

        if (!empty($data["password"])) {
            $data["password"] = md5($data["password"]);
        }
        $managerModel->save($data);
        return success("修改成功");
    }

    //获取管理员列表


    //管理员登陆
    public function loginManager()
    {
        $data = input('post.');
        try {
            validate(UserValidate::class)->scene('add')->check($data);
        } catch (\Exception $e) {
            // 验证失败 输出错误信息
            return success($e->getError());
        }
        $data['password'] = md5($data['password']);
        $managerModel = ManagerModel::where('username', $data['username'])->where('password', $data['password'])->find();
        if (empty($managerModel)) {
            return fail('账号或密码错误');
        }

        //heard头的token
        $token = JwtUtil::encode($managerModel["id"], config('jwtConfig.secretKey'));


//        $userModer = UserModel::where('username', $data['username'])->where('password', $data['password'])->find();
//        $cachePerm = $managerModel['id'] . 'perm';
        $cacheToken = $managerModel['id'] . 'token';
//        Cache::set($cachePerm,$arr);//以秒为单位
        Cache::set($cacheToken, $token['access_token']);
        return success($token);
    }


    //管理员退出登陆
    public function outLoginManager()
    {
        $id = request()->uid;
        $cacheToken = $id . 'token';
        Cache::delete($cacheToken);
        return success('退出登陆成功');
    }


    public function sc()
    {
        $id = request()->uid;
        $data = input("post.");
        $cc = [
            "scid" => $id,
            "sc" => $data["sc"]
        ];
        $sc = new SCModel();
        $sc->save($cc);
        return success("收藏成功");
    }

    public function scs()
    {
        $id = request()->uid;
        $managerModel = SCModel::Where("scid", $id)->select();
        return success($managerModel);
    }

    public function yj()
    {
        $data = input('post.');
        $yj = new YJModel();
        $yj->save($data);
        return success("提交成功");
    }

    public function syyj()
    {
        $managerModel = YJModel::select();
        return success($managerModel);
    }

    public function cxzhongyao()
    {
        $data = input('post.');
        $managerModel = ZYModel::where("name", $data['name'])->find();
        if (empty($managerModel)) {
            return success("当前中药不存在");
        }
        return success($managerModel);
    }

    public function cxfangji()
    {
        $data = input('post.');
        $managerModel = FJModel::where("name", $data['name'])->find();
        if (empty($managerModel)) {
            return success("当前方剂不存在");
        }
        return success($managerModel);
    }
}