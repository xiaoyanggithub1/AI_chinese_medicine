<?php


namespace app\admin\controller;

use app\admin\models\BannerModel;
use app\admin\models\PictureModel;
use app\BaseController;

class UploadCommonController extends BaseController
{
    public function upload()
    {
        $file = $_FILES['file'];
        $type = substr($file['name'], strpos($file['name'], '.') + 1);
//        $file_size = 100000 * 5;//5M

        if ($file["type"] != "image/png" && $file["type"] != "image/jpeg") {
            return fail('只允许上传图片');
        }

        if ($type != "png" && $type != "jpg") {
            return fail('只允许上传jpg图片');
        }
//        if ($file['size'] > $file_size) {
//            return fail('图片文件过大不允许上传！');
//        }
        $filePath = 'img/' . date('Y') . '/' . date('m') . '/' . date('d');
//        return success($filePath);
        if (!is_dir($filePath)) {
            mkdir($filePath, 0777, true);
        }
        $fileName = '/' . md5($file['name'] . time()) . '.' . $type;
        if (move_uploaded_file($file['tmp_name'], $filePath . $fileName)) {
            $pictureModel = new PictureModel();
            $data['path'] = $filePath . $fileName;
            $data['name'] = $file['name'];
            $data['size'] = $file['size'];
            $pictureModel->save($data);
            return success($filePath . $fileName);
        }
        return fail('图片上传失败！');
    }
}

