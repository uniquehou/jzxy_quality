from django.db import models
from quality import base

class Department(models.Model):
    name = models.CharField(u'院系名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '院系'
        verbose_name_plural = '院系'


class Major(models.Model):
    department = models.ForeignKey("Department", models.SET_NULL, verbose_name=u'所属院系', null=True, blank=True)
    name = models.CharField(u'专业名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业'


class Grade(models.Model):
    major = models.ForeignKey("Major", on_delete=models.SET_NULL, verbose_name=u'所属专业', null=True, blank=True)
    name = models.CharField(u'班级名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'


class Student(models.Model):
    sex_choice = (
        ('1', '男'),
        ('2', '女')
    )
    nation_choice = (
        ('1', '汉族'),
        ('2', '壮族'),
        ('3', '满族'),
        ('4', '回族'),
        ('5', '苗族'),
        ('6', '维吾尔族'),
        ('7', '土家族'),
        ('8', '彝族'),
        ('9', '蒙古族'),
        ('10', '藏族'),
        ('11', '布依族'),
        ('12', '侗族'),
        ('13', '瑶族'),
        ('14', '朝鲜族'),
        ('15', '白族'),
        ('16', '哈尼族'),
        ('17', '哈萨克族'),
        ('18', '黎族'),
        ('19', '傣族'),
        ('20', '畲族'),
        ('21', '傈僳族'),
        ('22', '仡佬族'),
        ('23', '东乡族'),
        ('24', '高山族'),
        ('25', '拉祜族'),
        ('26', '水族'),
        ('27', '佤族'),
        ('28', '纳西族'),
        ('29', '羌族'),
        ('30', '土族'),
        ('31', '仫佬族'),
        ('32', '锡伯族'),
        ('33', '柯尔克孜族'),
        ('34', '达斡尔族'),
        ('35', '景颇族'),
        ('36', '毛南族'),
        ('37', '撒拉族'),
        ('38', '布朗族'),
        ('39', '塔吉克族'),
        ('40', '阿昌族'),
        ('41', '普米族'),
        ('42', '鄂温克族'),
        ('43', '怒族'),
        ('44', '京族'),
        ('45', '基诺族'),
        ('46', '德昂族'),
        ('47', '保安族'),
        ('48', '俄罗斯族'),
        ('49', '裕固族'),
        ('50', '乌孜别克族'),
        ('51', '门巴族'),
        ('52', '鄂伦春族'),
        ('53', '独龙族'),
        ('54', '塔塔尔族'),
        ('55', '赫哲族'),
        ('56', '珞巴族'),
    )
    political_satus_choice = (
        ('1', '群众'),
        ('2', '共青团员'),
        ('3', '预备党员'),
        ('4', '共产党员'),
        ('5', '其它')
    )


    # student_major = models.ForeignKey("Major", on_delete=models.SET_NULL, verbose_name=u'专业', null=True, blank=True)
    student_id = models.CharField(u'学号', max_length=20, default=' ', unique=True)
    password = models.CharField(u'密码', max_length=100, default=base.encodepass('111111'))
    student_name = models.CharField(u'姓名', max_length=30, default=' ')
    sex = models.CharField(u'性别', max_length=1, choices=sex_choice, default='1')
    nation = models.CharField(u'民族', max_length=2, choices=nation_choice, default='1')
    student_department = models.ForeignKey("Department", on_delete=models.SET_NULL, verbose_name='院系', null=True, blank=True)
    student_grade = models.ForeignKey("Grade", on_delete=models.SET_NULL, verbose_name=u'班级', null=True, blank=True)
    political_satus = models.CharField(u'政治面貌', max_length=1, default='1', choices=political_satus_choice)
    duty = models.CharField(u'职务', max_length=100, blank=True, default='')

    address = models.CharField(u'住址', max_length=100, default='', blank=True)
    contact = models.CharField(u'本人联系方式', max_length=20, default='', blank=True)
    parent_contact = models.CharField(u'亲属联系方式', max_length=20, default='', blank=True)

    account = models.CharField(u'一卡通卡号', max_length=30, blank=True)

    def __str__(self):
        return self.student_name

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'


class Term(models.Model):
    name = models.CharField(u'学期', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学期'
        verbose_name_plural = '学期'


class Praise(models.Model):
    name = models.CharField(u'素质拓展类型', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '素质拓展类型'
        verbose_name_plural = '素质拓展类型'


class PraiseRecord(models.Model):
    standard_choice = (
        ('1', '国家级'),
        ('2', '省级'),
        ('3', '校级'),
        ('4', '学院级')
    )
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, verbose_name=u'当前学期', null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')
    praise_type = models.ForeignKey(Praise, on_delete=models.SET_NULL, verbose_name=u'类型', null=True)
    standard = models.CharField(u'级别', max_length=2, blank=True, default='', choices=standard_choice)
    text = models.CharField(u'说明', max_length=100, default='')
    description = models.CharField(u'补充说明', max_length=1000, blank=True)
    image = models.ImageField(u'图片', upload_to='praise', blank=True)
    praise_time = models.DateField(u'时间', blank=True, auto_now=True)

    def __str__(self):
        return self.student.student_name + "-" + self.praise_type.name

    class Meta:
        verbose_name = '素质拓展记录'
        verbose_name_plural = '素质拓展记录'


class Publishment(models.Model):
    name = models.CharField(u'违规违纪类型', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '违规违纪类型'
        verbose_name_plural = '违规违纪类型'

class PublishmentRecord(models.Model):
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, verbose_name=u'当前学期', null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')
    publish_type = models.ForeignKey(Publishment, on_delete=models.SET_NULL, verbose_name=u'类型', null=True)
    text = models.CharField(u'说明', max_length=100, default='')
    description = models.CharField(u'补充说明', max_length=1000, blank=True)
    image = models.ImageField(u'图片', upload_to='media/publish', blank=True)
    publish_time = models.DateField(u'时间', blank=True, auto_now=True)

    def __str__(self):
        return self.student.student_name + "-" + self.publish_type.name

    class Meta:
        verbose_name = '违规违纪记录'
        verbose_name_plural = '违规违纪记录'


class Remark(models.Model):
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, verbose_name=u'当前学期', null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')
    text = models.TextField(u'评定内容', default='空')

    def __str__(self):
        return f"{self.term.name} - {self.student.student_name}"

    class Meta:
        verbose_name = '素质评定'
        verbose_name_plural = '素质评定'
