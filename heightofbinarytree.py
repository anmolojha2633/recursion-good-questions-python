def height(root):
    if root==None:
        return 0;
    leftstheight=height(root.left)
    rightstheight=height(root.right)
    return max(leftstheight,rightstheight)+1
    