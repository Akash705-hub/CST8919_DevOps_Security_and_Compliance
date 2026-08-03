# Cloud Governance Gone Rogue – Azure Policy Lab

## Lab Summary

This lab introduces Azure Policy as a way to enforce organizational governance and security controls in Microsoft Azure. In the scenario, MapleTech Solutions is growing quickly and needs to prevent developers from deploying resources in an uncontrolled way. The goal of the lab is to create and assign Azure Policies that enforce key business rules, including restricting deployments to Canada Central, requiring a mandatory tag, and blocking public IP creation.

By completing this lab, you will learn how to:
- Create custom Azure Policies
- Group policies into a Policy Initiative
- Assign the initiative to a resource group
- Enforce compliance using Deny effects

## Video


## Lab Objectives

- Create and assign Azure Policies and a Policy Initiative
- Enforce region restriction to Canada Central
- Enforce a mandatory ProjectName tag
- Prevent the creation of public IP addresses
- Test enforcement with sample deployments

## Explanation of Each Policy

### 1. Region Lockdown Policy
- Name: Only-CanadaCentral
- Effect: Deny
- Purpose: This policy ensures that resources can only be deployed in the Canada Central region.
- Why it matters: It helps the organization maintain regional compliance, reduce deployment sprawl, and align resources with business and legal requirements.

### 2. Mandatory Tagging Policy
- Name: Require-ProjectName-Tag
- Effect: Deny
- Purpose: This policy requires every resource to include the ProjectName tag.
- Why it matters: Tags help with cost tracking, ownership, resource management, and reporting. Requiring a tag improves governance and accountability across the environment.

### 3. Block Public IP Policy
- Name: Deny-Public-IP
- Effect: Deny
- Purpose: This policy prevents the creation of Public IP resources.
- Why it matters: Blocking public IP addresses strengthens security by reducing the chance of exposing services directly to the internet.

## Policy Initiative

The lab also includes creating a Policy Initiative named MapleTech Secure Foundation. This initiative groups the three policies together so they can be assigned and enforced as a single set of governance controls.

## Assignment and Enforcement

After creating the policies and initiative, the initiative is assigned to a resource group with enforcement mode set to Enforce. This ensures that any deployment that violates the defined rules will be blocked automatically.
