/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *ptr1 = list1;
        ListNode *ptr2 = list2;

        ListNode *head = new ListNode();
        ListNode *curr = head;

        while (ptr1 && ptr2) {
            if (ptr1 -> val < ptr2 -> val) {
                curr -> next = ptr1;
                curr = curr -> next;
                ptr1 = ptr1 -> next;
            } else {
                curr -> next = ptr2;
                curr = curr -> next;
                ptr2 = ptr2 -> next;
            }
        }

        if (ptr1) {
            while (ptr1) {
                curr -> next = ptr1;
                ptr1 = ptr1 -> next;
                curr = curr -> next;
            }

            return head -> next;
        }

        if (ptr2) {
            while (ptr2) {
                curr -> next = ptr2;
                ptr2 = ptr2 -> next;
                curr = curr ->next;
            }

            return head -> next;
        }

        return head -> next;
    }
};
