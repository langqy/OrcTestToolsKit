# -*- coding: utf-8 -*-
from datetime import datetime

from OrcLib.LibCommon import is_null
from OrcLib.LibException import OrcDatabaseException

from OrcLib.LibDatabase import TabCaseDet
from OrcLib.LibDatabase import gen_id
from OrcLib.LibDatabase import orc_db
from OrcApi.Case.StepDefMod import StepDefMod


class CaseDetMod():
    """
    Test data management
    """
    __session = orc_db.session

    def __init__(self):

        self.__step = StepDefMod()

    def usr_search(self, p_filter=None):
        """
        :param p_filter:
        :return:
        """
        _res = self.__session.query(TabCaseDet)

        if 'id' in p_filter:
            _res = _res.filter(TabCaseDet.id == p_filter['id'])

        if 'case_id' in p_filter:
            _res = _res.filter(TabCaseDet.case_id == p_filter['case_id'])

        if 'step_id' in p_filter:
            _res = _res.filter(TabCaseDet.step_id == p_filter['step_id'])

        return _res.all()

    def usr_add(self, p_data):
        """
        Add item
        :param p_data:
        :return:
        """
        _case_id = p_data["case_id"]
        _step_id = p_data["step_id"]

        _node = TabCaseDet()

        # Create id
        _node.id = gen_id("case_det")

        # case_id
        _node.case_id = _case_id

        # step_id
        _node.step_id = _step_id

        # create_time, modify_time
        _node.create_time = datetime.now()

        try:
            self.__session.add(_node)
        except:
            raise OrcDatabaseException

        self.__session.commit()

        return _node

    def usr_update(self, p_cond):

        for t_id in p_cond:

            if "id" == t_id:
                continue

            _data = None if is_null(p_cond[t_id]) else p_cond[t_id]
            _item = self.__session.query(TabCaseDet).filter(TabCaseDet.id == p_cond['id'])
            _item.update({t_id: _data})

        self.__session.commit()

    def usr_delete(self, p_id):

        self.__session.query(TabCaseDet).filter(TabCaseDet.id == p_id).delete()
        self.__session.commit()

    def usr_list_search(self, p_id_list):

        _res = self.__session.query(TabCaseDet).filter(TabCaseDet.id.in_(p_id_list))
        return _res.all()