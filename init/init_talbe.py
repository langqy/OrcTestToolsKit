# coding=utf-8
from OrcApi import orc_db

from OrcLib.LibDatabase import LibDictionary
from OrcLib.LibDatabase import LibSequence

from OrcLib.LibDatabase import LibWidgetType
from OrcLib.LibDatabase import LibWidgetOperation


init_value_dictionary = [
    LibDictionary(dict(id="10001", dict_flag="batch_type", dict_order="1",
                       dict_value="GROUP", dict_text=u"计划组", dict_desc=u"用于存放批量计划")),
    LibDictionary(dict(id="10002", dict_flag="batch_type", dict_order="2",
                       dict_value="BATCH", dict_text=u"计划", dict_desc=u"单个计划")),

    LibDictionary(dict(id="10003", dict_flag="case_type", dict_order="1",
                       dict_value="GROUP", dict_text=u"用例组", dict_desc=u"用于存放批量用例")),
    LibDictionary(dict(id="10004", dict_flag="case_type", dict_order="2",
                       dict_value="CASE", dict_text=u"用例", dict_desc=u"单个用例")),
    LibDictionary(dict(id="10005", dict_flag="case_type", dict_order="3",
                       dict_value="FUNC", dict_text=u"函数", dict_desc=u"用例但不能单独执行")),

    LibDictionary(dict(id="10006", dict_flag="step_type", dict_order="1",
                       dict_value="NORMAL", dict_text=u"普通", dict_desc=u"普通步骤")),
    LibDictionary(dict(id="10007", dict_flag="step_type", dict_order="1",
                       dict_value="FUNC", dict_text=u"函数", dict_desc=u"函数步骤")),

    LibDictionary(dict(id="10008", dict_flag="item_type", dict_order="1",
                       dict_value="WEB", dict_text="WEB", dict_desc="")),
    LibDictionary(dict(id="10009", dict_flag="item_type", dict_order="2",
                       dict_value="IOS", dict_text="IOS", dict_desc="")),
    LibDictionary(dict(id="10010", dict_flag="item_type", dict_order="3",
                       dict_value="ANDROID", dict_text="ANDROID", dict_desc="")),
    LibDictionary(dict(id="10011", dict_flag="item_type", dict_order="4",
                       dict_value="JSON", dict_text=u"JSON接口", dict_desc="")),
    LibDictionary(dict(id="10012", dict_flag="item_type", dict_order="5",
                       dict_value="WEBSERVICE", dict_text="WEBSERVICE", dict_desc="")),

    LibDictionary(dict(id="10013", dict_flag="item_mode", dict_order="1",
                       dict_value="OPERATE", dict_text=u"操作项", dict_desc=u"执行操作")),
    LibDictionary(dict(id="10014", dict_flag="item_mode", dict_order="2",
                       dict_value="CHECK", dict_text=u"检查项", dict_desc=u"执行检查")),

    LibDictionary(dict(id="10015", dict_flag="data_mode", dict_order="1",
                       dict_value="STR", dict_text=u"字符", dict_desc="")),
    LibDictionary(dict(id="10016", dict_flag="data_mode", dict_order="2",
                       dict_value="INT", dict_text=u"整数", dict_desc="")),
    LibDictionary(dict(id="10017", dict_flag="data_mode", dict_order="3",
                       dict_value="SQL", dict_text="SQL", dict_desc="")),

    LibDictionary(dict(id="10018", dict_flag="data_type", dict_order="1",
                       dict_value="INP", dict_text=u"输入", dict_desc="")),
    LibDictionary(dict(id="10019", dict_flag="data_type", dict_order="2",
                       dict_value="OUT", dict_text=u"输出", dict_desc="")),
    LibDictionary(dict(id="10020", dict_flag="data_type", dict_order="3",
                       dict_value="CHK", dict_text=u"检查", dict_desc="")),


    LibDictionary(dict(id="10021", dict_flag="widget_attr_type", dict_order="1",
                       dict_value="ID", dict_text="ID", dict_desc="")),
    LibDictionary(dict(id="10022", dict_flag="widget_attr_type", dict_order="2",
                       dict_value="NAME", dict_text="NAME", dict_desc="")),
    LibDictionary(dict(id="10023", dict_flag="widget_attr_type", dict_order="3",
                       dict_value="XPATH", dict_text="XPATH", dict_desc="")),
    LibDictionary(dict(id="10024", dict_flag="widget_attr_type", dict_order="4",
                       dict_value="TAGNAME", dict_text=u"标签名称", dict_desc="")),
    LibDictionary(dict(id="10025", dict_flag="widget_attr_type", dict_order="5",
                       dict_value="LINK_TEXT", dict_text=u"链接文字", dict_desc="")),
    LibDictionary(dict(id="10026", dict_flag="widget_attr_type", dict_order="6",
                       dict_value="CSS", dict_text="CSS", dict_desc="")),

    LibDictionary(dict(id="10027", dict_flag="src_type", dict_order="1",
                       dict_value="BATCH", dict_text=u"计划", dict_desc="")),
    LibDictionary(dict(id="10028", dict_flag="src_type", dict_order="2",
                       dict_value="CASE", dict_text=u"用例", dict_desc="")),
    LibDictionary(dict(id="10029", dict_flag="src_type", dict_order="3",
                       dict_value="STEP", dict_text=u"步骤", dict_desc="")),
    LibDictionary(dict(id="10030", dict_flag="src_type", dict_order="4",
                       dict_value="ITEM", dict_text=u"执行项", dict_desc="")),

    LibDictionary(dict(id="10031", dict_flag="operate_object_type", dict_order="1",
                       dict_value="PAGE", dict_text=u"页面", dict_desc="")),
    LibDictionary(dict(id="10032", dict_flag="operate_object_type", dict_order="2",
                       dict_value="WIDGET", dict_text=u"控件", dict_desc="")),

    LibDictionary(dict(id="10033", dict_flag="run_def_type", dict_order="1",
                       dict_value="BATCH", dict_text=u"计划", dict_desc="")),
    LibDictionary(dict(id="10034", dict_flag="run_def_type", dict_order="2",
                       dict_value="CASE", dict_text=u"用例", dict_desc="")),
    LibDictionary(dict(id="10035", dict_flag="run_def_type", dict_order="3",
                       dict_value="TEST", dict_text=u"执行记录", dict_desc="")),

    LibDictionary(dict(id="10036", dict_flag="run_det_type", dict_order="1",
                       dict_value="BATCH_GROUP", dict_text=u"计划组", dict_desc="")),
    LibDictionary(dict(id="10037", dict_flag="run_det_type", dict_order="2",
                       dict_value="BATCH", dict_text=u"计划", dict_desc="")),
    LibDictionary(dict(id="10038", dict_flag="run_det_type", dict_order="3",
                       dict_value="CASE_GROUP", dict_text=u"用例组", dict_desc="")),
    LibDictionary(dict(id="10039", dict_flag="run_det_type", dict_order="4",
                       dict_value="CASE", dict_text=u"用例", dict_desc="")),
    LibDictionary(dict(id="10040", dict_flag="run_det_type", dict_order="5",
                       dict_value="STEP", dict_text=u"步骤", dict_desc="")),
    LibDictionary(dict(id="10041", dict_flag="run_det_type", dict_order="6",
                       dict_value="ITEM", dict_text=u"步骤项", dict_desc="")),

    LibDictionary(dict(id="10042", dict_flag="test_env", dict_order="1",
                       dict_value="TEST", dict_text=u"测试环境", dict_desc="")),
    LibDictionary(dict(id="10043", dict_flag="test_env", dict_order="2",
                       dict_value="PRE", dict_text=u"预生产环境", dict_desc="")),
    LibDictionary(dict(id="10044", dict_flag="test_env", dict_order="3",
                       dict_value="PRD", dict_text=u"生产环境", dict_desc=""))]


init_value_sequence = [
    LibSequence(dict(id="20001", field_name="batch_def", field_seq="100000000")),
    LibSequence(dict(id="20002", field_name="batch_det", field_seq="110000000")),
    LibSequence(dict(id="20003", field_name="case_def", field_seq="200000000")),
    LibSequence(dict(id="20004", field_name="case_det", field_seq="210000000")),
    LibSequence(dict(id="20005", field_name="step_def", field_seq="220000000")),
    LibSequence(dict(id="20006", field_name="step_det", field_seq="230000000")),
    LibSequence(dict(id="20007", field_name="item", field_seq="240000000")),
    LibSequence(dict(id="20008", field_name="page_def", field_seq="300000000")),
    LibSequence(dict(id="20009", field_name="page_det", field_seq="310000000")),
    LibSequence(dict(id="20010", field_name="window_def", field_seq="320000000")),
    LibSequence(dict(id="20011", field_name="widget_def", field_seq="330000000")),
    LibSequence(dict(id="20012", field_name="widget_det", field_seq="340000000")),
    LibSequence(dict(id="20013", field_name="data", field_seq="400000000")),
    LibSequence(dict(id="20014", field_name="dict", field_seq="20000"))]

init_value_widget_type = [
    LibWidgetType(dict(id="30001", type_order=1, type_mode="PRO",
                       type_name="GROUP", type_text=u"控件组", type_desc="")),
    LibWidgetType(dict(id="30002", type_order=2, type_mode="PRO",
                       type_name="WINDOW", type_text=u"窗口", type_desc="")),
    LibWidgetType(dict(id="30003", type_order=3, type_mode="PRO",
                       type_name="FRAME", type_text=u"FRAME", type_desc="")),
    LibWidgetType(dict(id="30004", type_order=4, type_mode="PRO",
                       type_name="BLOCK", type_text=u"块", type_desc="")),
    LibWidgetType(dict(id="30005", type_order=5, type_mode="PRO",
                       type_name="INP", type_text=u"输入框", type_desc="")),
    LibWidgetType(dict(id="30006", type_order=6, type_mode="PRO",
                       type_name="BTN", type_text=u"按钮", type_desc="")),
    LibWidgetType(dict(id="30007", type_order=7, type_mode="PRO",
                       type_name="LINK", type_text=u"链接", type_desc="")),
    LibWidgetType(dict(id="30008", type_order=7, type_mode="PRO",
                       type_name="PAGE", type_text=u"页面", type_desc="")),
    LibWidgetType(dict(id="31000", type_order=8, type_mode="USR",
                       type_name="TEST", type_text="TEST", type_desc=u"测试用"))]

init_value_widget_operation = [
    LibWidgetOperation(dict(id="40001", type_name="PAGE", ope_order="1",
                            ope_name="GET", ope_text=u"打开", ope_desc="")),
    LibWidgetOperation(dict(id="40002", type_name="PAGE", ope_order="2",
                            ope_name="MAX", ope_text=u"最大化", ope_desc="")),
    LibWidgetOperation(dict(id="40003", type_name="BLOCK", ope_order="1",
                            ope_name="EXISTS", ope_text=u"存在", ope_desc="")),
    LibWidgetOperation(dict(id="40004", type_name="BLOCK", ope_order="2",
                            ope_name="CLICK", ope_text=u"点击", ope_desc="")),
    LibWidgetOperation(dict(id="40005", type_name="BLOCK", ope_order="3",
                            ope_name="GET_ATTR", ope_text=u"获取属性", ope_desc="")),
    LibWidgetOperation(dict(id="40006", type_name="BLOCK", ope_order="4",
                            ope_name="GET_TEXT", ope_text=u"获取值", ope_desc="")),
    LibWidgetOperation(dict(id="40007", type_name="BLOCK", ope_order="5",
                            ope_name="GET_HTML", ope_text=u"获取HTML", ope_desc="")),
    LibWidgetOperation(dict(id="40008", type_name="INP", ope_order="1",
                            ope_name="INPUT", ope_text=u"输入", ope_desc=""))]

orc_db.drop_all()
orc_db.create_all()

orc_db.session.add_all(init_value_widget_type)
orc_db.session.add_all(init_value_widget_operation)
orc_db.session.add_all(init_value_dictionary)
orc_db.session.add_all(init_value_sequence)

orc_db.session.commit()
