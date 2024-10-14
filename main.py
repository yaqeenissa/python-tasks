from Node import Node


class Solution(object):
    def removeElements(self, head: Node, val: int) -> Node:
        item = Node(next_node=head)
        pre, curr = item, head

        while curr:
            nxt = curr.next
            if curr.val == val:
                pre.next = nxt
            else:
                pre = curr
            curr = nxt

        return item.next


def main():
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(6)
    node5 = Node(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    head = node1
    solution = Solution()
    new_head = solution.removeElements(head, 3)

    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    main()