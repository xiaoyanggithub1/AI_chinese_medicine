<?php


namespace app\admin\models;


use think\Model;

class PictureModel extends Model
{
    protected $name = 'picture';
    protected $pk = 'id';

    //将图片变成使用状态
//    public static function changeTmgToUse($path)
//    {
//        $pictureModel = self::where("path", $path)->find();
//        if (empty($pictureModel)) {
//            return;
//        }
//        $pictureModel->save(['status' => 0]);
//    }
//
//    //将图片变成未使用状态
//    public static function changeImgToNoUse($path)
//    {
//        $pictureModel = self::where("path", $path)->find();
//        if (empty($pictureModel)) {
//            return;
//        }
//        $pictureModel->save(['status' => 1]);
//    }
}