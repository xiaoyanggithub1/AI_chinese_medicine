<?php
// +----------------------------------------------------------------------
// | ThinkPHP [ WE CAN DO IT JUST THINK ]
// +----------------------------------------------------------------------
// | Copyright (c) 2006~2018 http://thinkphp.cn All rights reserved.
// +----------------------------------------------------------------------
// | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
// +----------------------------------------------------------------------
// | Author: liu21st <liu21st@gmail.com>
// +----------------------------------------------------------------------
use think\facade\Route;

Route::post('loginManager', 'ManagerController/loginManager')->allowCrossDomain();


Route::group(function () {
    Route::post('upload', 'UploadCommonController/upload');
})->middleware(\app\admin\middleware\LoginMiddleware::class);


Route::post('managers', 'ManagerController/managers')->allowCrossDomain();
Route::group('manager', function () {
    Route::post('getManagers', 'ManagerController/getManagers');
    Route::post('sc', 'ManagerController/sc');
    Route::post('scs', 'ManagerController/scs');
    Route::post('yj', 'ManagerController/yj');
    Route::post('cxzhongyao', 'ManagerController/cxzhongyao');
    Route::post('cxfangji', 'ManagerController/cxfangji');
    Route::post('syyj', 'ManagerController/syyj');
    Route::post('updateManagers', 'ManagerController/updateManagers');
    Route::post('outLoginManager', 'ManagerController/outLoginManager');
})->middleware(\app\admin\middleware\LoginMiddleware::class);
