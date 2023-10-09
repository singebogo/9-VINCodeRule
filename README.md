# 9-VINCodeRule
## 车架号第九位校验码规则国家标准


### 车架号（VIN）的组成。
    仅能采用阿拉伯数字和大写罗马字母：1、2、3、4、5、6、7、8、9、0、A 、B 、C 、D、E、F、G、H、J、K、L、M、N、P、R、S、T、U、V、W、X、Y、Z组成。其中，I、O和Q不能使用（避免不必要的混淆）。
    
## 车架号（VIN）中的第9位-校验位
  先说明计算规则：
        从车架号（VIN）的第一位开始，轮询每一位的字母或数字，用字母或数字的对应值*该位的加权值。
        计算全部17位的乘积相加除以11。所得的余数，即为该车架号（VIN）第9位正确的核验值。
          如果第9位和核验值相同，说明校验通过；
          如果不相同，说明校验不通过.

#### 给出字母数字的对应值表：
![image](https://github.com/singebogo/9-VINCodeRule/assets/位的加权值表.png)

#### 给出位的加权值表：
![image](https://github.com/singebogo/9-VINCodeRule/assets/字母数字的对应值表.png)

### 举个例子：
  WBAXW1104J0X16755，验证如下：
  （6*8+2*7+1*6+7*5+6*4+1*3+1*2+0*10+4*0+1*9+0*8+7*7+1*6+6*5+7*4+5*3+5*2）%（取余数）11 = 4
  核验值即为4,该VIN码的第9位校验位也是4。说明VIN码校验成功。如果余数等于10的话，就用X来进行替换。
  
### 源码
    src/
		VehicleIdentificationNumber.py: 车架号第九位校验码规则
			check_vin：检查给定的VIN是否符合规则
			get_normal_vin：生成一个符合规则VIN
		VinGuiMain.py: GUI图形界面
	dest/
		VinRule9Gui.exe: 可执行文件
	assets/     静态文件
			

### 运行效果图
![image](https://github.com/singebogo/9-VINCodeRule/assets/9-VINRules.png)
