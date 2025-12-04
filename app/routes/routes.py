apiVersion = "/api"

user = apiVersion + '/user'
product = apiVersion + '/product'


class Auth:
    auth = apiVersion + '/auth'
    login = auth + '/login'
    logout = auth + '/logout'
    register = auth + '/register'
    refresh = auth + '/refresh'
    current_user = auth + '/current-user'
class User:
    user = apiVersion + '/user'
    list_user = user + '/list'
    get_user = user + '/get'
    search = user + '/search'
    create = user + '/create'
    update = user + '/update'
    delete = user + '/delete'
    update_status = user + '/update_status'
    
class Customer:
    customer = apiVersion + '/customer'
    list_customer = customer + '/list'
    get_customer = customer + '/get'
    search = customer + '/search'
    create = customer + '/create'
    update = customer + '/update'
    delete = customer + '/delete'
    update_status_cliente = customer + '/update-status-cliente'
    create_complete = customer + '/create_complete'

class Property:
    _property = apiVersion + '/property'
    list_property = _property + '/list'
    get_property = _property + '/get'
    create = _property + '/create'
    update = _property + '/update'
    delete = _property + '/delete'
    add_inquilinos = _property + '/add_inquilinos' 
    get_inquilinos = _property + '/get_inquilinos' 
    list_by_cliente = _property + '/list_by_cliente'
    update_status_property = _property + '/update-status-propiedad'
    check_principal = _property + '/check-principal'
    check_duplicate = _property + '/check-duplicate'
    traspaso = _property + '/traspaso'

class Parameters: 
    param = apiVersion + '/param'
    list_params = param + '/list'
    create = param + '/create'
    update = param + '/update'
    delete = param + '/delete'
    list_by_parent = param + '/list_by_parent'
    list_by_module = param + '/list_by_module'
class Role: 
    role = apiVersion + '/role'
    list_roles = role + '/list'
    create = role + '/create'
    update = role + '/update'
    delete = role + '/delete'
    
class Permission: 
    permission = apiVersion + '/permission'
    list_permissions = permission + '/list'
    create = permission + '/create'
    update = permission + '/update'
    delete = permission + '/delete'

class RolePermission:
    role_permission = apiVersion + '/role_permission'
    list_role_permissions = role_permission + '/list'
    create = role_permission + '/create'
    update = role_permission + '/update'
    delete = role_permission + '/delete'
    
class Area: 
    area = apiVersion + '/area'
    list_area = area + '/list'
    create = area + '/create'
    update = area + '/update'
    delete = area + '/delete'  
    
class Item: 
    item = apiVersion + '/item'
    rpt = item + '/rpt'
    list_item = item + '/list'
    create = item + '/create'
    update = item + '/update'
    delete = item + '/delete'
    rpt_detailed_by_item = rpt + '/detailed_by_item'
    
class Rate:
    rate = apiVersion + '/rate'
    list_rate = rate + '/list'
    get_rate = rate + '/get'  
    create = rate + '/create'
    update = rate + '/update'
    delete = rate + '/delete'
    
class Outflow:
    outflow = apiVersion + '/outflow'
    rpt = outflow + '/rpt'
    list_outflow = outflow + '/list'
    get_outflow = outflow + '/get'
    search = outflow + '/search'
    create = outflow + '/create'
    update = outflow + '/update'
    delete = outflow + '/delete'
    state = outflow + '/state'
    rpt_quarterly = rpt + '/quarterly'
    rpt_cash_outflow_detail = rpt + '/cash_outflow_detail'
    rpt_payment_notice = rpt + '/payment_notice'
    #grafico/resumen
    rpt_summary_graphic_out_flow = rpt + '/summary_graphic_out_flow'

class Donation:
    donation = apiVersion + '/donation'
    list_donation = donation + '/list'
    get_donation = donation + '/get'
    create = donation + '/create'
    update = donation + '/update'
    delete = donation + '/delete'

class Repository:
    repository = apiVersion + '/repository'

    list_pending = repository + '/list_pending'
    list_invoiced = repository + '/list_invoiced'
    list_justified = repository + '/list_justified'
    
    create_extraordinary = repository + '/create_extraordinary'
    justify_charge = repository + '/justify_charge'
    process_payment = repository + '/process_payment'
    generate_monthly = repository + '/generate_monthly'
    verify_extraordinaries = repository + '/verify_extraordinaries'
    process_batch_payment = repository + '/process_batch_payment'
    get_voucher = repository + '/get_voucher'
    check_property_debt = repository + '/check_property_debt'
    check_customer_debts = repository + '/check_customer_debts'
    generate_monthly_on_reactivation = repository + '/generate_monthly_on_reactivation'
    list_vouchers = repository + '/list_vouchers'
    get_vouchers_detail = repository + '/get_voucher_detail'

class Income:
    income = apiVersion + '/income'
    rpt = income + '/rpt'
    
    list_incomes = income + '/list'
    list_by_type = income + '/list_by_type'
    list_by_date_range = income + '/list_by_date_range'
    get_income = income + '/get'
    
    report_global = income + '/report_global'
    report_by_categoria = income + '/report_by_categoria'
    rpt_payment_notice = rpt + '/payment_notice'
    rpt_income_receipt = rpt + '/income_receipt'
    rpt_income_receipt_list = rpt + '/income_receipt_list'
    #lista usuario-grafico-fecha corte-balance
    rpt_user_list = rpt + '/user_list'
    rpt_scheduled_cutoff = rpt + '/scheduled_cutoff'
    rpt_summary_graphic = rpt + '/summary_graphic'
    rpt_balance_summary = rpt + '/balance_summary'
    rtp_income_by_category = rpt + '/by_category'
    rpt_individual_debts = rpt + '/individual_debts'
    rpt_last_payment = rpt + '/last_payment'

class Param_Income:
    param_income = apiVersion + '/param_income'
    verify = param_income + '/verify'
    create = param_income + '/create'
    get_income = param_income + '/list'
    get_by_month = param_income + '/get_month'