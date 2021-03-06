INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (1, 'case_type', '1', 'GROUP', '用例组', '用于存放批量用例');
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (2, 'case_type', '2', 'CASE', '用例', '单个用例');
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (3, 'data_mode', '1', 'STR', '字符', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (4, 'data_mode', '2', 'INT', '整数', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (5, 'data_mode', '3', 'SQL', 'SQL', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (6, 'data_type', '1', 'INP', '输入', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (7, 'data_type', '2', 'OUT', '输出', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (8, 'data_type', '3', 'CHK', '检查', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (9, 'item_type', '1', 'WEB', 'WEB', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (10, 'item_type', '2', 'IOS', 'IOS', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (11, 'item_type', '3', 'ANDROID', 'ANDROID', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (12, 'item_type', '4', 'JSON', 'JSON接口', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (13, 'item_type', '5', 'WEBSERVICE', 'WEBSERVICE', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (14, 'item_mode', '1', 'OPERATE', '操作项', '执行操作');
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (15, 'item_mode', '2', 'CHK', '检查项', '执行检查');
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (16, 'item_operator_type', '1', 'INPUT', '输入', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (17, 'item_operator_type', '2', 'SUBMIT', '点击', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (18, 'widget_type', '1', 'WINDOW', '窗口', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (19, 'widget_type', '2', 'FRAME', 'FRAME', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (20, 'widget_type', '3', 'INP', '输入框', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (21, 'widget_type', '4', 'BTN', '按钮', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (22, 'widget_type', '5', 'LINK', '链接', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (23, 'widget_type', '6', 'SPAN', 'SPAN', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (24, 'widget_attr_type', '1', 'ID', 'ID', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (25, 'widget_attr_type', '2', 'NAME', 'NAME', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (26, 'widget_attr_type', '3', 'XPATH', 'XPATH', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (27, 'widget_attr_type', '4', 'TAGNAME', 'TAGNAME', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (28, 'src_type', '1', 'BATCH', '批', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (29, 'src_type', '2', 'CASE', '用例', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (30, 'src_type', '3', 'STEP', '步骤', null);
INSERT INTO lib_dictionary(id, dict_flag, dict_order, dict_value, dict_text, dict_desc) VALUES (31, 'src_type', '4', 'ITEM', '执行项', null);

commit;