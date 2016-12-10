def readfile(cl ='CustomerList.txt'):
    if cl:
        try:
            fp = open(cl, 'r')
        except IOError:
            print "Error opening file"
            return None
        else:
            customer_list = []
            data = fp.readlines()
            for customer in data:
                c = customer.split('\n')[0]
                c = c.split(',')
                customer_list.append(c)
            fp.close()
            return customer_list


def match_customer(input_id, customer_list):
    for customer in customer_list:
        if customer[0] == input_id:
            return customer

    return None


def print_no(num):
    print "(%s) %s-%s" % (num[:3], num[3:6], num[6:])


def print_customer_detail(customer):
    print
    print customer[0], customer[2] + ",", customer[1]
    print customer[3]
    print customer[4] + ',', customer[5], customer[6]
    print_no(customer[7])
    print


def rc():
    input_id = raw_input("Enter ID number: ")
    customer = match_customer(input_id, customer_list)

    if customer:
        print_customer_detail(customer)
        confirmation = raw_input("Confirm (Y/N): ")
        if confirmation == 'Y' or confirmation == 'y':
            return customer
    print 'Customer ID not found'
    return []


def nc():
    print "\nWelcome, new Customer!"


def gc():
    print "Welcome and please enjoy, Guest User"
    print "Enjoy our complimentary features available to you \n"


def main():

    selection = 0
    while selection >= 0:
        print "---------------------------------"
        print "1) Returning Customer"
        print "2) New Customer"
        print "3) Guest"
        print "---------------------------------\n"

        selection = int(raw_input("Please select your customer type: "))

        if selection == 1:
            customer = rc()
            selection = -1
        elif selection == 2:
            customer = nc()
            selection = -1
        elif selection == 3:
            gc()
            selection = -1
        else:
            print "\nPlease enter your customer type from a value 1-3:"
            selection = 0


if __name__ == '__main__':
    customer_list = readfile('CustomerList.txt')
    main()
