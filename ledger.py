from xml.etree import ElementTree as eletree
import os


default = 'ledger.xml'    # default directory for ledger

def check_ledger():
    """checks to make sure the ledger exists"""
    if os.path.exists(default):
        return True

def search_ledger(ssn):
    """searches the ledger based off of a social security number"""
    ledger = eletree.parse(default).getroot()
    for patient in ledger.findall('SSN'):
        if patient.find('SSN').text == ssn:
            first_name = patient.find('FirstName').text
            last_name = patient.find('LastName').text
            visit_date = patient.find('DOB').text
            treatment = patient.find("Treatment").text
            rx = patient.find('Prescription').text
            diag = patient.find('Diagnosis').text
            return [first_name, last_name, visit_date, treatment, rx, diag]

def handle_process():
    """gets the process ID"""
    return os.getpid()

def handle_hash():
    """returns the previous has from the ledger"""
    ledger = eletree.parse(default).getroot()
    return ledger[-1][3].text

def handle_sha256p():
    """returns the previous hash from the ledger"""
    ledger = eletree.parse(default).getroot()
    return ledger[-1][2].text

def build_ledger():
    """build initial ledger file"""
    root = eletree.Element('BlockLedger')
    ledger = eletree.ElementTree(root)
    ledger.write(default)
    return 0

def add_to_ledger(ID,chash, phash, ssn, fname, dob, tx, rx, pid, lname, diag):
    """adds new items to the ledger"""
    if os.path.exists(default):
        ledger = eletree.parse(default)
        ledger_root = ledger.getroot()
        child = eletree.SubElement(ledger_root, 'BlockRecord')
        eletree.SubElement(child, "BlockID").set("BlockID", ID)
        eletree.SubElement(child, "ProcessID").set("ProcessID", pid)
        eletree.SubElement(child, "PreviousHash").set("PreviousHash", phash)
        eletree.SubElement(child, "BlockHash").set("BlockHash", chash)
        eletree.SubElement(child, "DOB").set("DOB", dob)
        eletree.SubElement(child, "FirstName").set("FirstName", fname)
        eletree.SubElement(child, "LastName").set("LastName", lname)
        eletree.SubElement(child, "SSN").set("SSN", ssn)
        eletree.SubElement(child, "Diagnosis").set("Diagnosis", diag)
        eletree.SubElement(child, "Prescription").set("Prescription", rx)
        eletree.SubElement(child, "Treatment").set("Treatment", tx)
        ledger.write(default)
    else:
        build = build_ledger()
        if build == 0:
            add_to_ledger(ID, chash, phash, fname, lname, ssn, tx, rx, pid, dob, diag)
    return 0