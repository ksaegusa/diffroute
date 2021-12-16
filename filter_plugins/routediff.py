import ipaddress
#!/usr/bin/python
class FilterModule(object):
  def pop_uptime(self, input_value):
    output = list()
    for i in input_value:
      i.pop('UPTIME')
      output.append(i)
    return output

  def ip_sort(self, input_value):
      output =  sorted(input_value, key=lambda x: ipaddress.IPv4Address(x['NETWORK']))
      return output

  def network_sort(self, input_value):
      output =  sorted(input_value, key=lambda x: int(x['MASK']))
      return output

  def ip_network_sort(self, input_value):
      output =  sorted(input_value, key=lambda x: ipaddress.IPv4Network(x['NETWORK'] + '/' + x['MASK']))
      return output

  def filters(self):
      return {
          'sort_ip_filter': self.ip_sort,
          'sort_network_filter': self.network_sort,
          'sort_ip_network_filter': self.ip_network_sort,
          'pop_uptime': self.pop_uptime,
      }
