from xml.dom import minidom # used to parse xml files
from xml.etree import ElementTree as eletree
import xml.etree.cElementTree as led # used for creating the ledger in xml


default = ''    # default directory for ledger


def get_previous():
    """returns previous transaction in the ledger"""
    # TODO write ths to parse ledger to get previous transaction hash
    previous_transaction = ""
    index = 1
    return [previous_transaction, index]

def check_ledger():
    """checks the ledger for previous transaction"""
    # TODO WRITE CHECKING OF LEDGER FOR PREVIOUS TRANSACTION

    return False

def parse_ledger(previous='sha256p'):
    ledg = eletree.parse(default).getroot()

def get_info(ssn):
    """returns the data for a given social security number"""
    # may not use
    ledger = eletree.parse(default).getroot()
    for child in ledger:
        for grand_child in child:
            if grand_child.attrib.contains(ssn):
                return child.attrib

def handle_ledger(ssn):
    ledger = eletree.parse(default).getroot()
    for patient in ledger.findall('country'):
        if patient.find('ssn').text == ssn:
            first_name = patient.find('fname').text
            last_name = patient.find('lname').text
            visit_date = patient.find('vdate').text
            treatment = patient.find("treatment").text
            rx = patient.find('rx').text

def handle_process():
    return 0

def handle_hash():
    ledger = eletree.parse(default).getroot()
    return ledger[-1][2].text

def handle_sha256p():
    ledger = eletree.parse(default).getroot()
    return ledger[-1][3].text

def handle_fname():
    return 0

def handle_lname():
    return 0

def handle_rx():
    return 0

def handle_treat():
    return 0

def handle_ssn():
    return 0

def handle_date():
    return 0

def handle_time():
    return 0

def handle_uuid():
    return 0

#todo write the xml add and creation functions