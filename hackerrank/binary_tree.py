class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def check_binary_search_tree_(root):
    if(root.left != None and root.right != None):
        left = get_all_nodes(root.left)
        right = get_all_nodes(root.right)
        if min(right) < max(left):
            return False
        else:
            return check_binary_search_tree_(root.right) and check_binary_search_tree_(root.left)
    elif(root.left != None):
        return check_binary_search_tree_(root.left)
    elif(root.right != None):
        return check_binary_search_tree_(root.right)
    else:
        return True

def get_all_nodes(root):
    output = [root.data]
    if (root.left != None):
        output.append(root.left.data)
        output = output + get_all_nodes(root.left)
    if(root.right != None):
        output.append(root.right.data)
        output = output + get_all_nodes(root.right)
    return output
