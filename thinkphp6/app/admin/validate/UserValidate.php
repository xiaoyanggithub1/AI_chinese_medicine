<?php


namespace app\admin\validate;


use think\Validate;

class UserValidate extends Validate
{
    protected $rule =   [
        'username'  => 'require|min:2|max:50',
//        'password'  => 'require|min:5',
        'name'  => 'require|min:2',
        'age'   => 'number|min:0',
//        'phone'  => 'require|phone',
        'gender'  => 'number|between:0,1',
        'email' => 'email',
        'studentNum'=> 'require|min:2|max:50'
    ];
    protected $scene = [
        'add'  =>  ['username','password'],
        'update'  =>  ['username','password','name','age','phone','gender','email'],
        'new' =>   ['username','password','age','gender','email'],
        'news' =>   ['studentNum'],
    ];
}