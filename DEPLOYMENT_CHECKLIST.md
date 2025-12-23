# Deployment Checklist

Use this checklist when deploying the Google Classroom Blender Add-on to your class.

## Pre-Deployment (1-2 hours)

### 1. Google Cloud Setup ☐
- [ ] Create Google Cloud project
- [ ] Enable Google Classroom API
- [ ] Enable Google Drive API
- [ ] Configure OAuth consent screen
  - [ ] Choose Internal (for schools) or External
  - [ ] Fill in app information
  - [ ] Add required scopes (handled automatically)
- [ ] Create OAuth 2.0 Desktop credentials
- [ ] Download credentials.json

### 2. Test Installation ☐
- [ ] Install Blender 4.5 LTS (if not already installed)
- [ ] Install Python dependencies to Blender's Python
- [ ] Install add-on in Blender
- [ ] Add credentials.json to config folder
- [ ] Restart Blender
- [ ] Verify add-on appears in sidebar (press N)

### 3. Test Full Workflow ☐
- [ ] Sign in with Google
- [ ] Verify courses appear
- [ ] Create test assignment in Google Classroom
- [ ] Attach test .blend file to assignment
- [ ] In Blender: Refresh courses
- [ ] In Blender: Select course
- [ ] In Blender: Refresh assignments
- [ ] In Blender: Open assignment file
- [ ] Make changes to file
- [ ] Save file
- [ ] Submit assignment from Blender
- [ ] Verify submission appears in Google Classroom
- [ ] Test sign out and sign back in

### 4. Prepare Distribution Materials ☐
- [ ] Copy credentials.json to distribution folder
- [ ] Prepare installation instructions (use INSTALL_GUIDE.md)
- [ ] Create class-specific quick start guide (customize QUICK_REFERENCE.md)
- [ ] Prepare troubleshooting FAQ (use TROUBLESHOOTING.md)
- [ ] Optional: Create video tutorial
- [ ] Optional: Create slide presentation for class demo

### 5. Prepare Support Resources ☐
- [ ] Set up help channel (email, forum, class discussion)
- [ ] Prepare FAQs based on common issues
- [ ] Identify student helpers/tech assistants
- [ ] Schedule office hours for installation help
- [ ] Create backup submission method (traditional Google Classroom)

## Student Distribution (Week 1)

### Day 1: Preparation Class (45-60 min) ☐
- [ ] Explain the add-on and its benefits
- [ ] Demonstrate the workflow
- [ ] Distribute credentials.json securely
- [ ] Share installation instructions
- [ ] Assign homework: Install and test

### Day 2-3: Installation Support ☐
- [ ] Provide installation time in lab
- [ ] Help students with:
  - [ ] Python dependency installation
  - [ ] Add-on installation in Blender
  - [ ] Credentials file placement
  - [ ] First authentication
- [ ] Document common issues encountered
- [ ] Update FAQ with solutions

### Day 4: Test Assignment ☐
- [ ] Create simple test assignment (e.g., "Add a cube")
- [ ] Students open, complete, and submit from Blender
- [ ] Verify all students can complete workflow
- [ ] Help students who have issues
- [ ] Collect feedback

### Day 5: Review and Adjust ☐
- [ ] Address remaining issues
- [ ] Update documentation based on feedback
- [ ] Ensure backup submission method is clear
- [ ] Ready for regular use

## Ongoing Maintenance

### Weekly ☐
- [ ] Monitor submission patterns
- [ ] Address new issues promptly
- [ ] Update FAQ as needed

### Monthly ☐
- [ ] Review API usage quota (if approaching limits)
- [ ] Check for Google API updates
- [ ] Gather student feedback
- [ ] Update documentation

### Semester End ☐
- [ ] Collect feedback for next semester
- [ ] Update setup process based on lessons learned
- [ ] Consider rotating credentials for security
- [ ] Archive this semester's configuration

## Emergency Procedures

### If Add-on Stops Working ☐
1. [ ] Check Google service status
2. [ ] Verify API quotas not exceeded
3. [ ] Check credentials not revoked
4. [ ] Fall back to traditional submission
5. [ ] Notify students of workaround
6. [ ] Debug and fix issue
7. [ ] Resume normal operations

### If Students Can't Submit ☐
1. [ ] Verify assignment deadline not passed
2. [ ] Check assignment settings in Google Classroom
3. [ ] Confirm internet connectivity
4. [ ] Provide alternative submission method
5. [ ] Investigate specific issues
6. [ ] Document solution

### If Credentials Compromised ☐
1. [ ] Revoke old credentials in Google Cloud Console
2. [ ] Generate new credentials
3. [ ] Distribute new credentials.json to class
4. [ ] Have students replace file and re-authenticate
5. [ ] Update documentation

## Success Metrics

Track these to measure deployment success:

### Week 1 ☐
- [ ] % students successfully installed
- [ ] % students completed test submission
- [ ] Number of support requests

### Week 2-4 ☐
- [ ] % assignments submitted via add-on
- [ ] Average time to submit
- [ ] Student satisfaction (survey)
- [ ] Number of issues per week

### Ongoing ☐
- [ ] Submission rate via add-on vs. traditional
- [ ] Time saved per assignment
- [ ] Student feedback scores
- [ ] Issue resolution time

## Troubleshooting Contacts

List your support resources:

- Teacher: _______________
- Email: _______________
- Office hours: _______________
- Lab assistant: _______________
- Tech support: _______________

## Notes Section

Use this space for class-specific notes:

```
Date: _______________
Class: _______________
Students: _______________

Specific configuration:
- Blender version: _______________
- Google Workspace domain: _______________
- Special considerations: _______________

Common issues encountered:
1. _______________
2. _______________
3. _______________

Solutions implemented:
1. _______________
2. _______________
3. _______________
```

## Resources

- Installation Guide: INSTALL_GUIDE.md
- Teacher Guide: TEACHER_GUIDE.md
- Troubleshooting: TROUBLESHOOTING.md
- Quick Reference: QUICK_REFERENCE.md
- Project Summary: PROJECT_SUMMARY.md

## Post-Deployment Review

After first full semester:

- [ ] Overall success rating: ___ / 10
- [ ] Would use again: Yes / No
- [ ] Major improvements needed: _______________
- [ ] What worked well: _______________
- [ ] What didn't work: _______________
- [ ] Suggestions for next semester: _______________

---

**Remember**: Have a backup plan! Traditional Google Classroom submission should remain available as a fallback.
