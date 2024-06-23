<?php


namespace app\admin\models;


use app\admin\pivot\ManagerRolePivot;
use think\Model;

class ManagerModel extends Model
{
    protected $name = 'manager';
    protected $pk = 'id';




    //获取当前登录管理员信息


    public static function getAdminInfo($id)
    {
        return self::
//        where('status', 1)
        where("id", $id)
//            ->where("del_flag", 0)
            ->with(["roles"])->hidden(['roles' => ['pivot'], 'password']);
    }
}