/*********************************************************************************************************************
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
*********************************************************************************************************************/

#include <stdio.h>

 struct ListNode {
     int val;
     struct ListNode *next;
 };



struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2)
{
    if(NULL == l1) return l2;
    if(NULL == l2) return l1;
	struct ListNode* listOutputhead = NULL;
	if (l1->val > l2->val)
	{
		listOutputhead = l2;
		l2 = l2->next;
	}
	else
	{
		listOutputhead = l1;
		l1 = l1->next;
	}

	struct ListNode *listOutput = listOutputhead;
	while(NULL != l1 && NULL != l2)
	{
		if (l1->val < l2->val)
		{
			listOutput->next=l1;
			l1 = l1->next;
		}
		else
		{
			listOutput->next = l2;
			l2 = l2->next;
		}
		listOutput = listOutput->next;

		if(NULL != l1) listOutput->next = l1;
		if(NULL != l2) listOutput->next = l2;
	}

	return listOutputhead;
}

int main(int argc, char const *argv[])
{
	struct ListNode *listInput1;
	struct ListNode *listInput2;
	struct ListNode *listOutput;
	struct ListNode l11, l12, l13, l21, l22, l23;
	l11.val = 1;
	l11.next = &l12;

	l12.val = 2;
	l12.next = &l13;

	l13.val = 4;
	l13.next = NULL;

	l21.val = 1;
	l21.next = &l22;

	l22.val = 3;
	l22.next = &l23;

	l23.val = 4;
	l23.next = NULL;

	listInput1 = &l11;
	listInput2 = &l21;
	// print the number of two lists before merge
	printf("From first list: ");
	for(;NULL != listInput1; listInput1=listInput1->next)
		printf("%d ", listInput1->val);
	printf("\n");

	printf("From second list: ");
	for(;NULL != listInput2; listInput2=listInput2->next)
		printf("%d ", listInput2->val);
	printf("\n");

	listOutput = mergeTwoLists(listInput1, listInput2);

	printf("output list: ");
	for(;NULL != listOutput; listOutput=listOutput->next)
		printf("%d ", listOutput->val);
	printf("\n");
	return 0;
}